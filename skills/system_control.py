import os
import datetime
import time
from core.speaker import speak

# Define known applications and their paths
APP_PATHS = {
    "chrome": r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk",
    "vscode": r"C:\\Users\\gaura\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code",
    "notepad": "notepad.exe",
    "excel": r"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
    "word": r"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    "cmd": "cmd.exe",
    "powershell": "powershell.exe",
    "paint": "mspaint.exe",
    "calculator": "calc.exe",
    "explorer": "explorer.exe"
}

APP_EXECUTABLES = {
    "chrome": "chrome.exe",
    "vscode": "Code.exe",
    "notepad": "notepad.exe",
    "excel": "EXCEL.EXE",
    "word": "WINWORD.EXE",
    "cmd": "cmd.exe",
    "powershell": "powershell.exe",
    "paint": "mspaint.exe",
    "calculator": "calc.exe",
    "explorer": "explorer.exe"
}


def open_app(app_name):
    if app_name in APP_PATHS:
        try:
            os.startfile(APP_PATHS[app_name])
            speak(f"Opening {app_name}")
        except Exception as e:
            speak(f"Couldn't open {app_name}.")
            print(e)
    else:
        speak(f"I don't know how to open {app_name} yet.")

def close_app(app_name):
    if app_name in APP_EXECUTABLES:
        exe = APP_EXECUTABLES[app_name]
        os.system(f"taskkill /f /im {exe}")
        speak(f"Closing {app_name}")
    else:
        speak(f"I don't know how to close {app_name}.")

def system_command(command):
    if "shutdown" in command:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 5")
    elif "restart" in command:
        speak("Restarting the system.")
        os.system("shutdown /r /t 5")
    elif "sleep" in command:
        speak("Putting the system to sleep.")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif "exit" in command or "quit" in command:
        speak("Exiting Jarvis. Goodbye!")
        exit()
    else:
        speak("Unknown system command.")

def set_alarm(time_str):
    speak(f"Setting an alarm for {time_str}")
    try:
        alarm_hour, alarm_minute = map(int, time_str.split(":"))
        while True:
            now = datetime.datetime.now()
            if now.hour == alarm_hour and now.minute == alarm_minute:
                speak("Wake up! Here's your alarm.")
                os.startfile("C:\\Windows\\Media\\Alarm01.wav")  # Use your own alarm file
                break
            time.sleep(30)
    except Exception as e:
        speak("Invalid time format. Please say time as HH:MM.")
        print(e)

def handle(query: str):
    query = query.lower()

    # System commands
    if "shutdown" in query:
        system_command("shutdown")
    elif "restart" in query:
        system_command("restart")
    elif "sleep" in query:
        system_command("sleep")
    elif "exit" in query or "quit" in query:
        system_command("exit")

    # App opening
    elif "open" in query:
        for app in APP_PATHS:
            if app in query:
                open_app(app)
                return
        speak("Which app do you want me to open?")

    # App closing
    elif "close" in query:
        for app in APP_EXECUTABLES:
            if app in query:
                close_app(app)
                return
        speak("Which app do you want me to close?")

    # Set alarm
    elif "set alarm" in query:
        speak("At what time should I set the alarm? Please say in HH:MM format.")
        from core.listener import listen
        alarm_time = listen()
        set_alarm(alarm_time)

    else:
        speak("I'm not sure what system task you want me to perform.")
