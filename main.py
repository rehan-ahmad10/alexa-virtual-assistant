from voice import mic, speak
from system_control import open_apps, powerfunc
from web_search import news, search_google, search_youtube
from file_search import search_file
from ai import ai_process


def process_command(command):
    while True:
        if "open" in command:
            open_apps(command)
            break

        elif "news" in command:
            news()
            break

        elif "laptop" in command:
            powerfunc(command)
            break

        elif "ai" in command:
            ai_process()
            break

        elif "search in google" in command:
            search_google()
            break

        elif "search in youtube" in command:
            search_youtube()
            break

        elif "search in my files" in command or "search in my file" in command:
            search_file()
            break

        else:
            print("\nInvalid command")
            speak("Invalid command")

            print("Speak command")
            speak("Speak command")
            command = mic()

if __name__ == "__main__":
    print("\nInitializing Alexa...")
    speak("Initializing Alexa...")

    print("Say Alexa to activate system")
    speak("Say Alexa to activate system")

    while True:
        try:
            print("\nAlexa Active...")
            text = mic()
            if "alexa" in text:
                print("Yes sir ...")
                speak("Yes sir ...")

                command = mic()
                process_command(command)

        except Exception as e:
            print(f"eror is : {e}")