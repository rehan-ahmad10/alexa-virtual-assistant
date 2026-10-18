import os
import speech_recognition as sr
from pathlib import Path

from voice import mic, speak

translate_num = {
    1  : "one"   ,
    2  : "two"   ,
    3  : "three" ,
    4  : "four"  ,
    5  : "five"  ,
    6  : "six"   ,
    7  : "seven" ,
    8  : "eight" ,
    9  : "nine"  ,
    10 : "ten"
}


def search_file():
    while True:
        try:
            print("\nTell me what you want to search in my files")
            speak("Tell me what you want to search in my files")
            file_name = mic()

            path_list = []
            name_list = []

            disks = ["D:\\", "E:\\", "F:\\"]

            for disk in disks:
                if not Path(disk).exists():
                    continue
                for file in Path(disk).rglob("*"):
                    if file.is_file() and file_name in file.stem.lower():
                        path_list.append(str(file))

            len_files = len(path_list)

            if len_files > 10:
                print(f"I found {len_files} files")
                speak(f"I found {len_files} files")

                print("Invalid! Out of range")
                speak("Invalid! Out of range")
                break

            elif len_files > 1:
                print(f"I found {len_files} files")
                speak(f"I found {len_files} files")
                i = 1
                for file in path_list:
                    list1 = file.split("\\")

                    f_name = list1[len(list1) - 1]
                    name_list.append(f"{i}. {f_name}")
                    print(f"{i}. {f_name}")
                    speak(f"{i}. {f_name}")
                    i += 1

                print("Tell me which number file i open")
                speak("Tell me which number file i open")

                cond = True
                i = ""
                while cond:
                    num_file = mic()
                    for n in range(1, len_files + 1):
                        if translate_num[n] in num_file or str(n) in num_file:
                            i = n
                            cond = False
                            break
                    else:
                        print("Invalid!")
                        speak("Invalid!")

                        print("Speak Again")
                        speak("Speak Again")

                print(f"Opening file  : {name_list[i -1]}")
                speak(f"Opening file  : {name_list[i -1]}")

                os.startfile(path_list[i - 1])
                name = path_list[i - 1]
                f_list = name.split(".")
                if f_list[-1] == "mp3" or f_list[-1] == "mp4" or f_list[-1] == "webm":
                    input("Press Enter to continue using Alexa : ")
                    break
                else:
                    break

            elif len_files == 1:
                list1 = path_list[0].split("\\")
                f_name = list1[len(list1) - 1]

                print(f"Opening file  : 1. {f_name}")
                speak(f"Opening file  : 1. {f_name}")
                os.startfile(path_list[0])

                name = path_list[0]
                f_list = name.split(".")
                if f_list[-1] == "mp3" or f_list[-1] == "mp4" or f_list[-1] == "webm":
                    input("Press Enter to continue using Alexa : ")
                break

            else:
                print("Invalid! Command")
                speak("Invalid! Command")

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
            print(f"Error is : {e}")