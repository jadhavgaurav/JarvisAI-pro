import webbrowser
from core.speaker import speak

def handle(query: str):
    if "youtube" in query:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "google" in query:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    else:
        speak("I don't recognize that website.")
