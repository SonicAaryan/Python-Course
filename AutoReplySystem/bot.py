from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Load API key
api_key = os.getenv("API_KEY")
print("API key loaded:", api_key is not None)

# Initialize client
client = OpenAI(api_key=api_key)

command = '''
[10:32 pm, 16/4/2025] Samruddhi Tikambare Mgk: 1 may nanter bhetu divya pn yenar ahe
[10:35 pm, 16/4/2025] Divya Tayade: Haa
[10:28 am, 17/4/2025] Jay Shinde: Okk
[9:24 am, 21/4/2025] Samruddhi Tikambare Mgk: Happy Birthday Andya @Aniket Belgonkar 🌈
[9:44 am, 21/4/2025] Aniket Belgonkar: Thank you 🙏🏻
[10:02 am, 21/4/2025] ∆a༬yan_Sonar: Happy birthday andya🥳
[10:03 am, 21/4/2025] Aniket Belgonkar: Thank you 🙏🏻
[10:10 am, 21/4/2025] Divya Tayade: Happiest Birthday @Aniket Belgonkar ✨
[10:50 am, 21/4/2025] Aniket Belgonkar: Thank you 🙏🏻
'''
completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"You are person named aaryan who speak hindi as well as english . He is form india and is a coder . you analyze chat history and respon like aaryan!"},
        {"role":"system","content":command},
    ]
)
print(completion.choices[0].message)