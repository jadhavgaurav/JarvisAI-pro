import pyttsx3

# Initialize engine once
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Speech speed
engine.setProperty('volume', 1.0)  # Max volume

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Default voice (can customize)

def speak(text: str):
    """
    Convert text to speech and speak it out loud.
    """
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()
