import pyttsx3

engine = pyttsx3.init()
text = input("Name: ")
engine.say(f"Hello, everyone. {text}")
engine.runAndWait()