import os
import faq
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
load_dotenv()

HF_TOKEN = os.getenv('HF_TOKEN')

# Creates a client that talks to hugging face model
client = InferenceClient(
    # provider='hf-inference',
    api_key=HF_TOKEN
)

def get_ai_reply(user_message: str, history: list) -> str:
    try:
        # this sends your message ai model
        response = client.chat.completions.create(
            model="Qwen/Qwen2.5-7B-Instruct",
            messages =[
                {
                    'role': 'system',
                    'content':faq.get_system_prompt()
                },

                *history,

                {
                    'role':'user',
                    'content': user_message
                }
            ],
            max_tokens=150,
        )

        # Extract the text reply from response
        return response.choices[0].message.content.strip()
    except Exception as e:
        print('Error:',e)
        return "I'm having a technical issue. Please try again shortly."