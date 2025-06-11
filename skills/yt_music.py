import pywhatkit
from core.speaker import speak

def handle(query: str):
    song = query.replace("play", "").strip()
    if not song:
        speak("Please tell me the name of the song.")
        return
    speak(f"Playing {song} on YouTube.")
    pywhatkit.playonyt(song)
