import wikipedia 
from core.speaker import speak

def handle(query: str):
    try:
        topic = query.replace("who is", "").replace("what is", "").strip()
        result = wikipedia.summary(topic, sentences=2)
        speak("According to Wikipedia...")
        speak(result)
    except:
        speak("I couldn't find any information on that.")
