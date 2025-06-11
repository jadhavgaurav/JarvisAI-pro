from core.speaker import speak
from core.listener import listen

if __name__ == "__main__":
    speak("Hello, I am Jarvis Pro. How can I assist you?")
    query = listen()
    speak(f"You said: {query}")
    if query != "none":
        # Here you would typically route the query to the appropriate skill or handler
        speak("Processing your request...")
    else:
        speak("I didn't catch that. Please try again.")