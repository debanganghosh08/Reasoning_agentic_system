# File: agent_backend/model_loader.py

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel

def load_finetuned_model():
    """
    Loads the base Llama 3 model and applies the fine-tuned LoRA adapter from the local Drive path.
    """
    base_model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
    
    # This path is relative to the root project folder in Google Drive ('AGENT_DEV_DRIVE')
    # This will work correctly when the Colab notebook's working directory is changed.
    adapter_path = "llama-3-8b-hackathon-agent/checkpoint-48"

    print("Loading base model...")
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
    )

    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_id,
        quantization_config=bnb_config,
        device_map="auto",
    )
    
    tokenizer = AutoTokenizer.from_pretrained(base_model_id)
    tokenizer.pad_token = tokenizer.eos_token

    print(f"Applying fine-tuned adapter from: {adapter_path}")
    model = PeftModel.from_pretrained(base_model, adapter_path)
    print("Fine-tuned model loaded successfully!")

    return model, tokenizer