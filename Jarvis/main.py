import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
from dotenv import load_dotenv

# Initialize modules
recognizer = sr.Recognizer()
engine = pyttsx3.init()
pygame.mixer.init()

# Load environment variables
load_dotenv()
api_key = os.getenv("API_KEY")

# ✅ Safety check
if not api_key:
    raise ValueError("API_KEY not found in environment. Please set it in your .env file.")

# Voice output using gTTS
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

# AI interaction
def aiProcess(command):
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Keep responses short."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

# Handle commands
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        try:
            song = c.lower().split(" ", 1)[1]
            link = musicLibrary.music[song]
            webbrowser.open(link)
        except (IndexError, KeyError):
            speak("Sorry, I couldn’t find that song.")
    else:
        output = aiProcess(c)
        speak(output)

# Main loop
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        try:
            print("Listening for wake word...")
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
            word = recognizer.recognize_google(audio)
            print("Heard:", word)

            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Jarvis is active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except sr.WaitTimeoutError:
            continue  # No voice input within timeout
        except sr.UnknownValueError:
            print("Didn't catch that.")
        except Exception as e:
            print(f"Error: {e}")
