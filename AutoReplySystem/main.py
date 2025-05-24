import os
import pyautogui
import pyperclip
import time
from openai import OpenAI
from dotenv import load_dotenv
# import pygetwindow as gw

# Target Tab
# target_tab_keyword = "WhatsApp"  

# matching_window = "WhatsApp"

# for window in gw.getAllWindows():
#     print(window)


# Load .env
load_dotenv()

# Load API key
api_key = os.getenv("API_KEY")
print("API key loaded:", api_key is not None)

# Initialize client
client = OpenAI(api_key=api_key)


# Optional: a short pause after every PyAutoGUI call
pyautogui.PAUSE = 0.5

# Step 1: Click on the icon
pyautogui.click(x=3002, y=12)

# Step 2: Wait for any interface to load
time.sleep(1)

# Step 3: Click and drag to select text
pyautogui.moveTo(x=2600, y=213)
pyautogui.mouseDown()
pyautogui.moveTo(x=2600, y=1005, duration=1)
pyautogui.mouseUp()

# Step 4: Copy selected text
pyautogui.hotkey('ctrl', 'c')

# Step 5: Wait briefly for clipboard to update
time.sleep(0.5)

# Step 6: Retrieve copied text
copied_text = pyperclip.paste()

# Print or use the variable
print("Copied text:", copied_text)

completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"You are person named aaryan who speak hindi as well as english . He is form india and is a coder . you analyze chat history and respon like aaryan! but in cool way and short "},
        {"role":"system","content":copied_text},
    ]
)
# print(completion.choices[0].message)
response = completion.choices[0].message.content
pyperclip.copy(response)

# pyautogui.click(x=3141,y=1043)
# time.sleep(0.5)

pyautogui.hotkey('ctrl','v')
time.sleep(0.5)

pyautogui.press('enter')