import webbrowser
import requests
import speech_recognition as sr
from youtubesearchpython import VideosSearch

from api import newsapi
from voice import mic, speak

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"

def news():
    try:
        req = requests.get(url)
        if req.status_code == 200:
            news_data = req.json()

            articles = news_data.get("articles", [])
            print("\nNews are : ")
            speak("News are : ")

            for i in articles:
                print()
                print(i["description"])
                speak(i["description"])
                try:
                    rec = sr.Recognizer()
                    with sr.Microphone() as source:
                        print("\nListening....")
                        audio_data = rec.listen(source)
                        text = rec.recognize_google(audio_data)

                    print(f"Heard : {text}")
                    text = text.lower()
                    if "stop" in text:
                        break

                except Exception as e:
                    print()

        else:
            print(f"\nNews API error : {req.status_code}")
            speak("Sorry, I could not fetch the news")

    except Exception as e:
        print(f"\nError is : {e}")


def search_google():
    while True:
        try:
            print("\nTell me what you want to search in google")
            speak("Tell me what you want to search in google")
            text = mic()
            webbrowser.open(f"https://www.google.com/search?q={text}")

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


def search_youtube():
    while True:
        try:
            print("\nTell me what you want to search in youtube")
            speak("Tell me what you want to search in youtube")
            text = mic()
            videos_search = VideosSearch(text,limit=1)
            results = videos_search.result()

            if not results.get("result"):
                print("\nNo videos found")
                speak("No videos found")
                break
            
            video_id = results.get("result")[0]["id"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"

            webbrowser.open(video_url)
            print(f"\nPlaying video : ")

            speak(f"Playing video : ")
            input("Press Enter to continue using Alexa: ")
            break
            
        except Exception as e:
            print(f"\nError is : {e}")