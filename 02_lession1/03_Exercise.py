# Install an external module and use it to perform an operation of you like
import pyttsx3  # type:ignore
engine = pyttsx3.init()
engine.say("an AI by OpenAI")
engine.runAndWait()
