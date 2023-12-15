import speech_recognition as sr
import pyttsx3
import pyaudio
import platform
import datetime
import wikipedia
import pywhatkit

listener = sr.Recognizer()

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def command():
    try:
        with sr.Microphone as source:
            print("Im listening..... Waiting for a response")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "hello" in command:
                command= command.replace("hello", "")
    except:
        pass
    return command

def run_assistant():
    order = command()
    print(order)

    if 'time' in order:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("The current time is " + time)
    
    elif 'play' in order:
        play = order.replace('play', '')
        speak('Playing ' + play)
        pywhatkit.playonyt(play)

    elif "search" in order:
        search = order.replace("search", "")
        info = wikipedia.summary(search, 1)
        print(info)
        speak(info)

    elif "who is" in order:
        person = order.replace("who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)

    else:
        speak("I did not understand what you said. Please try again and speak clearly.")
    

        
