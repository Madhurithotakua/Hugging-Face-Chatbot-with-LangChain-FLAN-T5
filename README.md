# Hugging-Face-Chatbot-with-LangChain-FLAN-T5
# 🤖 Hugging Face Chatbot with LangChain + FLAN-T5

This is an interactive chatbot powered by [Hugging Face's](https://huggingface.co/) `google/flan-t5-large` model and integrated with [LangChain](https://www.langchain.com/) for tracing and monitoring.

---

## 🌟 Features

- Uses Hugging Face's `google/flan-t5-large` model for prompt-based text generation
- Instruction-tuned for better general-purpose performance
- LangChain `RunnableLambda` for seamless tracking with LangSmith
- Maintains chat history and context
- Loads API keys securely from `.env` file

---
## 🧠 What the Model Can Do

The `google/flan-t5-large` model is ideal for:

- 📚 General Knowledge Q&A  
- 🔄 Text Rewriting & Paraphrasing  
- 🌍 Language Translation  
- 🧮 Simple Math and Logic  
- ✍️ Grammar Correction  
- 🧾 Summarization  
- 🧠 Reasoning & Explanations  

---

## 📘 Key Concepts Explained

### 🧩 LangChain
LangChain is a powerful framework designed for building applications that utilize language models. It helps in:
- Connecting LLMs (Large Language Models) with external data and tools
- Managing prompt templates and chains
- Tracing and monitoring AI behavior via **LangSmith**
- Creating production-ready pipelines for chatbots, agents, and more

LangChain works like the "middleware" between your logic and the LLM.

---

### 🧠 `langchain_core.prompts`
This module contains tools for working with **Prompt Templates**.

- A `PromptTemplate` is like a blueprint for constructing prompts.  
- It allows you to define a structure, add variables, and reuse the prompt easily.

Example:
```python
PromptTemplate.from_template("Translate this into French: {text}")
