# import essential libraries
import requests # help us makes http calls to servers
import os # let us read environment variables
from dotenv import load_dotenv

load_dotenv()

# read the hugging facae api key from .env file
HF_TOKEN = os.getenv('HF_TOKEN')

# free ai model (Mistral-7B-instruct-v0.3) we're using on hugging face 
API_URL = 'https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3'

# deine a function for getting ai reply
def get_ai_reply(user_message: str) -> str:
    prompt = f""" You are a friendly customer support agent.
    Answer the customer helpfully and concisely in under 80 words.
    if you don't know something, say so honestly. 
    Don't hallucinate and give made-up answers to user.

    customer: {user_message}
    Agent: """

    # Authorization header tells HuggingFace "Yes I have an account"
    headers = {"Authorization": f"Bearer: {HF_TOKEN}"}

    # Payload is what we send to huggingface 
    payload = {
        "inputs": prompt,
        "parameters":{
            "max_new_tokens": 150, # max length of reply
            "temperature": 0.7, # 0 = robotic, 1 = creative
            "return_full_text": False, # it will only return the new reply, not our prompt

        }
    }

    # send request to Huggingface and wait for reply
    response = requests.post(API_URL, headers=headers, json=payload, timeout=30)

    # convert response to python dictionary
    result = response.json()
    try:
        # Huggingface API retruns a list of outputs, we will use the first item's text
        if isinstance(result, list) and 'generated_text' in result[0]:
            reply = result[0]['generated_text'].strip()
            return reply
            
        # Model is cold starting, api may retrun an error when model is just waking up
        if 'error' in result:
            return "⏳ AI is warming up! PLease send your message again in 10 Seconds"
    
    except requests.exceptions.Timeout:
        return "⏳ Taking too long to respond. Please try again."
    except Exception as e:
        return "Something went wrong. Please try again."


