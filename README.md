🛡️ AI Hallucination Firewall

A self-correcting LLM workflow built using LangGraph + LangChain to reduce hallucinations in AI-generated responses.

Instead of trusting a single model output, this system validates, scores, and conditionally rewrites responses using a structured state-machine architecture.

🚀 Why This Project?

Large Language Models can generate confident but incorrect information (hallucinations).

In production systems, especially in regulated domains (finance, healthcare, legal), blindly trusting LLM outputs is risky.

This project demonstrates how to move from simple prompt engineering to workflow engineering, where the system:

Generates

Validates

Scores

Self-corrects

before returning a response.

🧠 How It Works

The system follows a multi-step validation pipeline:

User Question
      ↓
Generate Answer
      ↓
Extract Factual Claims
      ↓
Verify Claims
      ↓
Score Hallucination Risk
      ↓
If Risk High → Rewrite → Revalidate
If Risk Low  → Return Final Answer


The process repeats until:

The answer meets a safety threshold

Or a maximum retry limit is reached

🏗️ Architecture

The workflow is implemented as a state machine using LangGraph.

Core Nodes

Generator – Produces initial LLM answer

Extractor – Breaks answer into factual claims

Verifier – Validates each claim independently

Scorer – Calculates hallucination risk score

Rewriter – Regenerates answer if risk exceeds threshold

Risk Calculation
Risk = 1 - (Verified Claims / Total Claims)


Higher risk → higher probability of hallucination.

⚙️ Why LangGraph?

Supports shared state across steps

Enables conditional routing

Allows retry loops

Prevents infinite execution with iteration caps

Makes complex AI workflows clean and modular

LangChain is used for LLM execution.
LangGraph orchestrates the workflow.

This separation improves scalability and maintainability.

🛠️ Tech Stack

Python 3.12+

LangChain

LangGraph

langchain-openai

OpenAI API

python-dotenv
