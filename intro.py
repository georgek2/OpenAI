import openai
from openai import OpenAI


'''
    Simple script to get started using OpenAI API
'''


# def chatgpt(prompt):
#     response = client.chat.completions.create(
#         model='gpt-3.5-turbo',
#         messages=[{'role': 'user', 'content': prompt}]
#     )
    
#     return response.choices[0].message.content.strip()


# if __name__ == '__main__':
#     while True:
#         user_prompt = input('You: ')
#         if user_prompt in ['quit', 'exit', 'bye']:
#             break 
#         response = chatgpt(user_prompt)
#         print('Chatgpt: ', response)
