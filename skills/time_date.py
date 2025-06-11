import datetime
from core.speaker import speak

def handle(query: str):
    if "time" in query:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
    elif "date" in query:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {today}")
