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

## Folder Structure

The repository is organized as follows:
