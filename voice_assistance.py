import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptxext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing......")
            data = recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print("not understand")


sptext()
