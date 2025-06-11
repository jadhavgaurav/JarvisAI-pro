import speech_recognition as sr

recognizer = sr.Recognizer()

def listen() -> str:
    """
    Listens to microphone input and converts it to text.
    Returns recognized string or "none".
    """
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 300
        audio = recognizer.listen(source)

    try:
        print("🔍 Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User: {query}")
        return query.lower()

    except sr.UnknownValueError:
        print("⚠️ Could not understand audio.")
        return "none"
    except sr.RequestError:
        print("⚠️ Speech service unavailable.")
        return "none"
