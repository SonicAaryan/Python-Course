from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("API_KEY"),
)
completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"You are a virtual assistant named jarvis skilled in general tasks like Alexa and google cloud.Give short responses"},
    ]
)
print(completion.choices[0].message)