import requests
from core.speaker import speak

def handle(query: str):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": query,
                "stream": False
            }
        )
        data = response.json()
        output = data.get("response", "Sorry, no response from LLM.")
        speak(output)
    except Exception as e:
        print("LLM ERROR:", e)
        speak("I'm unable to connect to the LLM engine.")
