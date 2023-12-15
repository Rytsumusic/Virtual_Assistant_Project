import speech_recognition as sr
import pyttsx3
import pyaudio

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to listen for the wake word "Hey Maggie"
def listen_for_wake_word():
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            # Use Google Speech Recognition to convert speech to text
            text = r.recognize_google(audio)
            if "hello" in text.lower():
                return True
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
        except sr.RequestError:
            print("Sorry, I'm having trouble with my speech recognition service.")


def respond():
    engine.say("How can I assist you?")
    engine.runAndWait()

text = ""  # Define the 'text' variable outside the function
while True:
    if listen_for_wake_word():
        if "nevermind" in text.lower() or "goodbye" in text.lower():
            engine.say("Goodbye!")
            engine.runAndWait()
            break
        else:
            respond()
