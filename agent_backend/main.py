# File: agent_backend/main.py

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from google.adk.agent import Agent
from google.adk.llm import Llm
from model_loader import load_finetuned_model
from tools import calculator

# --- 1. INITIALIZE APP AND LOAD MODEL ---
app = FastAPI(title="ADK-Powered Agent Backend")
model, tokenizer = load_finetuned_model()

# Wrap your custom Hugging Face model and tokenizer in the ADK Llm object
llm = Llm(model, tokenizer)

# --- 2. DEFINE THE AGENT'S PROMPT TEMPLATE ---
AGENT_PROMPT = """
You are a helpful and brilliant reasoning agent. Your goal is to solve the user's problem by thinking step-by-step.

You have access to the following tools:
{tools}

To solve the problem, you must use the following thinking process strictly:
1. **Thought:** First, think about the problem and devise a plan to solve it. Break the problem down into smaller, manageable steps.
2. **Action:** Based on your thought, decide if you need to use a tool. If so, output a single tool-use call in the format: `tool_name(arg1="value1", arg2="value2")`.
3. **Observation:** After you use a tool, the system will provide its output.
4. **Thought:** Analyze the observation and the previous steps to determine the next step in your plan.

Repeat this Thought/Action/Observation process until you have solved the problem.

Once you have the final answer, conclude with the following format:
**Final Answer:** [Your final, conclusive answer here]

Here is the user's problem:
{prompt}
"""

# --- 3. CREATE THE AGENT ---
agent = Agent(
    llm=llm,
    prompt_template=AGENT_PROMPT,
    tools=[calculator],
)

# --- 4. CREATE THE FASTAPI ENDPOINT ---
class Query(BaseModel):
    prompt: str

@app.post("/agent-generate")
async def agent_generate(query: Query):
    """
    This endpoint takes a user's prompt and runs the full agentic loop.
    """
    print(f"Received query: {query.prompt}")
    final_response = agent.run(query.prompt)
    
    return {"response": final_response}

# --- 5. RUN THE SERVER ---
# This part is primarily for local testing; the Colab script will handle running it.
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)