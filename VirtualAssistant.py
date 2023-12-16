import speech_recognition as sr
import pyttsx3
import datetime
import pyaudio
import wikipedia
import pywhatkit

listener = sr.Recognizer()

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def command():
    try:
        with sr.Microphone() as source:
            print("I'm listening... Waiting for a response")
            listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "hello" in command:
                command = command.replace("hello", "")
    except:
        return None
    return command

def run_assistant():
    order = command()
    if order is None:
        return run_assistant()

    print(order)

    if 'time' in order:
        time = datetime.datetime.now().strftime('%I%M %p')
        speak("The current time is " + time)
    
    elif'hello' in order:
        speak("Hello, how are you? My name is max. I am your virtual assistant. How can I help you?")
    
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
    
    elif "what is" in order:
        thing = order.replace("what is", "")
        info = wikipedia.summary(thing, 1)
        print(info)
        speak(info)
    
    elif "where is" in order:
        place = order.replace("where is", "")
        info = wikipedia.summary(place, 1)
        print(info)
        speak(info)
    
    elif any(keyword in order for keyword in ["goodbye", "nevermind", "bye"]):
        speak("Goodbye, have a nice day!")
        exit()
    
    else:
        speak("I did not understand what you said. Please try again and speak clearly.")
    
    return run_assistant()

run_assistant()
    

        
