import speech_recognition as sr
from gtts import gTTS
import pygame
import os

def mic():
    rec = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("\nListening....")
                audio_data = rec.listen(source)
                text = rec.recognize_google(audio_data)

            print(f"Heard : {text}")
            text = text.lower()

            if "stop" in text:
                exit()
            else:
                return text

        except Exception as e:
            print(f"Error is : {e}")


pygame.mixer.init()

def speak(text):
    try:
        tts = gTTS(text)
        tts.save("audio.mp3")

        pygame.mixer.music.load("audio.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()
        os.remove("audio.mp3")

    except Exception as e:
        print(f"\nError is : {e}")