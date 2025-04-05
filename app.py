import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from huggingface_hub import InferenceClient

# Load environment variables
load_dotenv()

# Load API keys
huggingface_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
langsmith_api_key = os.getenv("LANGCHAIN_API_KEY")  # ✅ Correct environment variable

if not huggingface_api_key:
    raise ValueError("❌ Hugging Face API key is missing. Check your .env file.")

if not langsmith_api_key:
    raise ValueError("❌ LangSmith API key is missing. Check your .env file.")

# ✅ Enable LangSmith tracing
os.environ["LANGCHAIN_TRACING_V2"] = "true"  
os.environ["LANGCHAIN_API_KEY"] = langsmith_api_key  # ✅ Required for LangSmith monitoring

# Initialize Hugging Face Inference Client
client = InferenceClient(model="google/flan-t5-large", token=huggingface_api_key)

# Chat history to maintain context
chat_history = [
    {"role": "system", "content": "You are a helpful AI assistant. Answer questions accurately and concisely."}
]

# Function to generate response from Hugging Face
def generate_response(user_input):
    prompt_text = f"User: {user_input}\nAI:"

    # Generate response using Hugging Face
    response = client.text_generation(prompt_text, max_new_tokens=200).strip()

    # Store conversation history
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": response})

    return response

# ✅ Wrap function inside a RunnableLambda for LangChain tracking
ask_question = RunnableLambda(lambda question: generate_response(question))

# Interactive Chatbot Loop
while True:
    user_input = input("\nMadhuri: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye! 👋")
        break

    response = ask_question.invoke(user_input)  # ✅ Using LangChain tracking
    print(f"Chatbot: {response}")
