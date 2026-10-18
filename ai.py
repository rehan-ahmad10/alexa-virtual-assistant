import speech_recognition as sr
from groq import Groq

from api import groqapi
from voice import mic, speak


client = Groq(api_key=groqapi)

def ai_process():
    while True:
        try:
            print("\nTell me what you want to search in AI")
            speak("Tell me what you want to search in AI")

            ai_search = mic()
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "Give me answer in exact and clear 2,3 sentences"
                    },
                    {
                        "role": "user",
                        "content": ai_search
                    }
                ],
                temperature=0.5,
            )
            print("\n", response.choices[0].message.content.strip())
            speak(response.choices[0].message.content.strip())

            print("If you want to search again, speak yes search again")
            speak("If you want to search again, speak yes search again")

            try:
                rec = sr.Recognizer()
                with sr.Microphone() as source:
                    print("\nListening....")
                    audio_data = rec.listen(source)
                    text = rec.recognize_google(audio_data)

                print(f"Heard : {text}")

                text = text.lower()
                if "stop" in text:
                    exit()

                if "yes" in text or "search" in text:
                    continue
                else:
                    break
            except Exception as e:
                break

        except Exception as e:
            print(f"\nError is : {e}")