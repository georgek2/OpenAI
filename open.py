import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_KEY", "")

prompt = input('You: ')

def openGPT(user_prompt: str):
    response = requests.post(
        url = "https://openrouter.ai/api/v1/chat/completions",
        headers = {
            "Authorization": api_key,
            "Content-Type": 'application/json'
        },
        
        data = json.dumps({
            'model': 'openai/gpt-4o-mini',
            'messages': [{
                'role': 'user',
                'content': user_prompt
            }]
        })
    )    

    result = response.json()['choices'][0]['message']['content']
    # result = response.json()

    return result


while True:
    if prompt in ['quit', 'exit', 'bye']:
        break
    print(openGPT(prompt))
    
    prompt = input('You: ')

