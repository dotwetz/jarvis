import speech_recognition as sr

import pyttsx3

import datetime

import webbrowser

import os

import random


recognizer = sr.Recognizer()

engine = pyttsx3.init()


def speak(text):

    engine.say(text)

    engine.runAndWait()


def listen():

    with sr.Microphone() as source:

        print("Listening for your command...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

        command = ""

        try:

            command = recognizer.recognize_google(audio)

            print(f"You said: {command}")

        except sr.UnknownValueError:

            print("Sorry, I didn't understand that.")

            speak("Sorry, I didn't catch that.")

        except sr.RequestError:

            print("Sorry, I'm having trouble connecting to the internet.")

            speak("Sorry, I can't connect to the internet.")

        return command.lower()


def execute_command(command):

    if "hello" in command:

        speak("Hello, how can I assist you today?")

    elif "time" in command:

        now = datetime.datetime.now()

        current_time = now.strftime("%H:%M:%S")

        speak(f"The current time is {current_time}")

    elif "open" in command:

        speak("Opening the website.")

        site = command.split("open ")[1]

        webbrowser.open(f"https://{site}")

    elif "play music" in command:

        speak("Playing some music.")

        music_folder = "/home/your_username/Music"

        songs = os.listdir(music_folder)

        song = random.choice(songs)

        os.system(f"xdg-open {os.path.join(music_folder, song)}")

    elif "stop" in command:

        speak("Goodbye!")

        exit()

    else:

        speak("Sorry, I didn't recognize that command.")


def run_jarvis():

    speak("Hello, I am Jarvis, your personal assistant.")

    while True:

        command = listen()

        execute_command(command)


if __name__ == "__main__":

    run_jarvis()
