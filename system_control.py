import webbrowser
import os
import ctypes

from voice import mic, speak


def open_apps(command):
    while True:
        try:

            if "whatsapp" in command:
                webbrowser.open("https://web.whatsapp.com/")
                break

            elif "deep seek" in command:
                webbrowser.open("https://chat.deepseek.com/")
                break

            elif "google" in command:
                webbrowser.open("https://google.com/")
                break

            elif "brave" in command:
                brave_path = r"C:\Users\Admin\OneDrive\Desktop\Brave.lnk"
                if os.path.exists(brave_path):
                    os.startfile(brave_path)
                else:
                    webbrowser.open("https://brave.com/")
                break

            elif "calculator" in command:
                os.startfile(r"C:\Windows\System32\calc.exe")
                break

            elif "clock" in command:
                os.startfile("ms-clock:")
                break

            elif "youtube" in command:
                webbrowser.open("https://youtube.com")
                break

            else:
                print("\nInvalid command")
                speak("Invalid command")

                print("Speak command")
                speak("Speak command")
                command = mic()

        except Exception as e:
            print(f"\nEror is : {e}")


def powerfunc(command):
    while True:
        try:

            if "screen off" in command:
                ctypes.windll.user32.SendMessageW(0xFFFF, 0x0112, 0xF170, 2)
                break

            elif "sleep" in command:
                ctypes.windll.powrprof.SetSuspendState(False, False, False)
                break

            elif "lock screen" in command:
                os.system("rundll32.exe user32.dll,LockWorkStation")
                break

            elif "restart" in command:
                os.system("shutdown /r /t 10")
                break

            elif "shutdown" in command:
                os.system("shutdown /s /t 10")
                break

            elif "screen on" in command:
                ctypes.windll.user32.mouse_event(0x0001, 1, 0, 0, 0)
                ctypes.windll.user32.mouse_event(0x0001, -1, 0, 0, 0)
                break

            else:
                print("Invalid command")
                speak("Invalid command")

                print("Speak command")
                speak("Speak command")

                command = mic()

        except Exception as e:
            print(f"\nError is : {e}")