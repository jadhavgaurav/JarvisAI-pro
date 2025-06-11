import wikipedia # type: ignore
from core.speaker import speak

def handle(query: str):
    # Restrict Wikipedia search to simple "who is"/"what is" questions under 6 words
    if query.startswith("who is") or query.startswith("what is"):
        words = query.split()
        if len(words) <= 6:
            topic = query.replace("who is", "").replace("what is", "").strip()
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak("According to Wikipedia...")
                speak(result)
                return
            except Exception:
                pass  # Allow fallback
    # Fallback to LLM if query is too long or not matched
    import skills.llm_chat as llm
    llm.handle(query)
