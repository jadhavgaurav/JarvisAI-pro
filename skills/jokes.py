import pyjokes # type: ignore
from core.speaker import speak

def handle(query: str):
    joke = pyjokes.get_joke()
    speak(joke)
