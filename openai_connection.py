import os
import dotenv
import openai

dotenv.load_dotenv("/Users/kovalov/Desktop/telegram-chatgpt-bot/.env")

openai_token = os.environ['CHATGPT_API_KEY']

openai.api_key=openai_token

messages = [{"role": "system", "content": "You are intelligent assistant."}]

while True:
    message = input("User: ")
    if message:
        messages.append({ "role": "user", "content": message},)
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choice[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})

