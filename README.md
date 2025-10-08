# Reasoning_agentic_system

### A Submission for the Saptang Labs Machine Learning Challenge

This repository contains the complete implementation of an Agentic AI system designed to solve complex, multi-step logical reasoning problems. The system leverages a fine-tuned Large Language Model within a structured agentic framework, enabling it to decompose problems, use tools, and provide transparent, step-by-step reasoning traces for its conclusions.

## Table of Contents
- [Project Overview](#project-overview)
- [System Architecture](#system-architecture)
- [Core Technologies](#core-technologies)
- [Folder Structure](#folder-structure)
- [Setup and Installation](#setup-and-installation)
- [How to Run the Agent](#how-to-run-the-agent)
- [Fine-Tuning Process](#fine-tuning-process)

## Project Overview

Standard Large Language Models (LLMs) often struggle with tasks requiring precise, multi-step logic. They can "hallucinate" intermediate steps or fail to follow a coherent plan. This project addresses these limitations by building an **agent** that doesn't just generate an answer, but actively *reasons* its way to a solution.

The agent operates on a **Thought-Action-Observation** loop:
1.  **Thought:** It analyzes the problem and devises a step-by-step plan.
2.  **Action:** It decides whether to use an external tool (like a calculator) to solve a sub-problem.
3.  **Observation:** It analyzes the output of the tool and incorporates the new information into its reasoning process.

This loop continues until the agent arrives at a final, verifiable answer.

## System Architecture

The system is composed of two main phases: a fine-tuning phase to specialize the model's reasoning capabilities, and a deployment phase where the agent is served via a web API.

*(Here, you can insert the architecture diagram we created earlier)*

1.  **Fine-Tuning:** The base `meta-llama/Meta-Llama-3-8B-Instruct` model was fine-tuned using Parameter-Efficient Fine-Tuning (PEFT/LoRA) on the provided `train.csv` dataset. This taught the model to generate high-quality, step-by-step reasoning traces.
2.  **Agent Backend:** The fine-tuned model is loaded into an agent built with the **Google Agent Development Kit (ADK)**. This agent is equipped with a `calculator` tool and is wrapped in a **FastAPI** web server, making it accessible via an API endpoint.

## Core Technologies

- **Programming Language:** Python
- **AI/ML Frameworks:** PyTorch, Hugging Face (Transformers, PEFT, Datasets)
- **Agent Framework:** Google Agent Development Kit (ADK)
- **Base LLM:** `meta-llama/Meta-Llama-3-8B-Instruct`
- **Fine-Tuned Adapter:** Hosted on Hugging Face at: **[your-hf-username/your-repo-name]** **(<- IMPORTANT: Add your Hugging Face link here!)**
- **Backend API:** FastAPI, Uvicorn

## Setup and Installation

To run this project, please follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/agentic-reasoning-system.git](https://github.com/your-username/agentic-reasoning-system.git)
    cd agentic-reasoning-system
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Authenticate with Hugging Face:**
    You will need a Hugging Face account and an access token to download the base model.
    ```bash
    huggingface-cli login
    ```

## How to Run the Agent

The agent is served via a FastAPI application. Due to the high RAM requirements of the model, it is strongly recommended to run the backend in a cloud environment with a GPU, such as Google Colab.

A Colab notebook is provided that contains the consolidated code to launch the server and expose it with `ngrok`.

If running locally (requires a powerful GPU and >16GB of RAM):

1.  Navigate to the backend directory:
    ```bash
    cd agent_backend
    ```

2.  Run the server using uvicorn:
    ```bash
    python -m uvicorn main:app --reload
    ```

3.  The API will be available at `http://127.0.0.1:8000`. You can access the interactive documentation at `http://127.0.0.1:8000/docs`.

## Fine-Tuning Process

The model was fine-tuned on the provided `train.csv` dataset to specialize its ability to generate step-by-step reasoning. The script `fine_tuning/finetune_agent.py` contains the complete code for this process, which was executed on a Google Colab T4 GPU. The script handles data formatting, PEFT/LoRA configuration, and training using the Hugging Face `Trainer`.
