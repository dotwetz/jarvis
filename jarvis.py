import pyttsx3
import speech_recognition as sr
import numpy as np
import noisereduce as nr

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    if "english" in voice.name.lower() and "uk" in voice.id.lower():
        engine.setProperty('voice', voice.id)
        break
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening for your command...")
        try:
            audio = recognizer.listen(source)
            audio_data = np.frombuffer(audio.get_raw_data(), np.int16)
            reduced_noise = nr.reduce_noise(y=audio_data, sr=16000)
            command = recognizer.recognize_google(sr.AudioData(reduced_noise.tobytes(), 16000, 2), language="en-GB")
            return command
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Speech recognition service error: {e}")
        except OSError as e:
            print(f"Audio system error: {e}")
        return None

if __name__ == "__main__":
    while True:
        command = listen()
        if command:
            if "shut up" in command.lower():
                speak("As you wish. Let me know if you need me.")
                break
            else:
                speak(f"You said: {command}")
