import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Set to British English voice
for voice in voices:
    if "english" in voice.name.lower() and "uk" in voice.id.lower():
        engine.setProperty('voice', voice.id)
        break

engine.setProperty('rate', 150)

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen and process voice input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening for your command...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language="en-GB")
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that.")
        except sr.RequestError:
            speak("There seems to be an issue with the speech service.")
        return None

# Main program loop
if __name__ == "__main__":
    while True:
        command = listen()
        if command:
            if "shut up" in command.lower():
                speak("As you wish. Let me know if you need me.")
                break
            else:
                speak(f"You said: {command}")
