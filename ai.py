import os
import faq
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY=os.getenv('GROQ_API_KEY')
HF_TOKEN = os.getenv('HF_TOKEN')

# Setup Groq Client
from groq import Groq
groq_client = Groq(api_key=GROQ_API_KEY)

# Setup Hugging Face Client
from huggingface_hub import InferenceClient
hf_client = InferenceClient(
    # provider='hf-inference',
    api_key=HF_TOKEN
)

def build_messages(user_message: str, history: list) -> list:
    """Builds messages list - same for both Groq and Huggging Face"""
    return [
        {
            "role": "system",
            "content": faq.get_system_prompt()
        },
        *history,
        {
            "role": "user",
            "content": user_message
        }
    ]

def try_groq(messages:list) -> str:
    """Try Groq first """
    response = groq_client.chat.completions.create(
        model='llama-3.1-8b-instant',
        messages=messages,
        max_tokens=150,
    )
    return response.choices[0].message.content.strip()

def try_huggingface(messages:list) -> str:
    "fallback to Hugging Face"
    response = hf_client.chat.completions.create(
            model="Qwen/Qwen2.5-7B-Instruct",
            messages=messages,
            max_tokens=150,
            )
    return response.choices[0].message.content.strip()


def get_ai_reply(user_message: str, history: list) -> str:
    messages = build_messages(user_message, history)
    # Try Groq first
    try:
        print('Trying Groq...')
        reply = try_groq(messages)
        if reply:
            print('Groq responded ✅')
            return reply
    except Exception as e:
        print('Groq failed', e)

    # Fallback to Hugging Face
    try:
        print('Trying HuggingFace....')
        reply = try_huggingface(messages)
        if reply:
            print('HuggingFace responded ✅')
            return reply
    except Exception as e:
        print('HuggingFace failed', e)
    
    # Both Failed
    return "I'm having a technical issue. Please try again shortly."