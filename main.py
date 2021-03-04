import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if "play" in command:
        video = command.replace('play', '')
        talk(f"I am playing {video}")
        pywhatkit.playonyt(video)
    elif "search" in command:
        search = command.replace('search', '')
        talk("okey, I will search")
        pywhatkit.search(search)
    elif 'about' in command:
        search = command.replace('about', '')
        talk(wikipedia.summary(search))


while True:
    run_alexa()
