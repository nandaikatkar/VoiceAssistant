import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change voice if needed
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print('Clearing background noises...Please wait')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything...')
        audio = recognizer.listen(source)
    return audio

def recognize_speech(audio):
    try:
        command = recognizer.recognize_google(audio)
        print(f'You said: {command}')
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        speak("Sorry, I could not understand the audio. Please try again.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        speak(f"Could not request results; {e}")
        return None

def execute_command(command):
    if 'chrome' in command:
        speak('Opening Chrome...')
        program = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        subprocess.Popen([program])
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak(f'The current time is {time}')
    elif 'play' in command:
        speak('Opening YouTube...')
        pywhatkit.playonyt(command)
    elif 'thankyou' in command:
        print('Welcomeee...')
        speak('welcome..I will be always available as your assistant..')    
    else:
        speak("Sorry, I didn't catch that. Please try again.")

def main():
    while True:
        audio = listen()
        command = recognize_speech(audio)
        if command:
            execute_command(command)

if __name__ == "__main__":
    main()
