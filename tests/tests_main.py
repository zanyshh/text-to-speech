# text to see if voices work on pyttsx3 module
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

# Try different voices
for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.say("Hello, world!")
    engine.runAndWait()
    print("Voice:", voice.name)