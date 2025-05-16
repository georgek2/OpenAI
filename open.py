import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_KEY", "")

prompt = input('You: ')

def openGPT(prompt):
    response = requests.post(
        url = "https://openrouter.ai/api/v1/chat/completions",
        headers = {
            "Authorization": api_key,
            "Content-Type": 'application/json'
        },
        
        data = json.dumps({
            'model': 'qwen/qwen3-4b:free', #openai/gpt-4o-mini
            'messages': [{
                'role': 'user',
                'content': prompt
            }]
        })
    )    

    result = response.json()['choices'][0]['message']['content']
    # result = response.json()

    return result 

print(openGPT(prompt))
