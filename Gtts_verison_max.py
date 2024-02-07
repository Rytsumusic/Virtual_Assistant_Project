import speech_recognition as sr
from gtts import gTTS
import datetime
import wikipedia
import pywhatkit
import playsound
import os

listener = sr.Recognizer()

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')
    playsound.playsound('output.mp3')

def get_command():
    try:
        with sr.Microphone() as source:
            print("I'm listening... Waiting for a response")
            listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "biddu" in command:
                command = command.replace("maggie", "")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand you. Please try again.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

    return command

def run_assistant():
    order = get_command()

    if order is None:
        return run_assistant()

    print(order)
    if 'hello' in order:
        speak("Hello, how are you? My name is Max. I am your virtual assistant. How can I help you?")

    elif 'time' in order:
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
    
    elif "timer" in order:
        timer = order.replace("timer", "")
        speak("Setting a timer for " + timer + " seconds")
        timer = int(timer)
        timer = timer * 60
        time.sleep(timer)
        speak("Your timer has ended")
    
    elif "add"+[item]+ "to a list" in order:
        item = order.replace("add", "")
        speak("Adding " + item + " to your list")
        with open("list.txt", "a") as f:
            f.write(item + "\n")
        f.close()
    
    elif "show me my list" in order:
        speak("Here is your list")
        with open("list.txt", "r") as f:
            print(f.read())
        f.close()
    
    elif"clear my list" in order:
        speak("Clearing your list")
        with open("list.txt", "w") as f:
            f.write("")
        f.close()
    
    elif "what is on my list" in order:
        speak("Here is your list")
        with open("list.txt", "r") as f:
            print(f.read())
        f.close()
    
    elif"open spotify on my desktop" in order:
        speak("Opening Spotify")
        os.system("open -a Spotify")

    elif any(keyword in order for keyword in ["goodbye", "nevermind", "bye"]):
        speak("Goodbye, have a nice day!")
        exit()

    else:
        speak("I did not understand what you said. Please try again and speak clearly.")

    return run_assistant()

run_assistant()
