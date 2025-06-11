from core.speaker import speak

# Intent → module mapping
INTENT_TO_SKILL = {
    "greet": "skills.greet",
    "time": "skills.time_date",
    "date": "skills.time_date",
    "joke": "skills.jokes",
    "play_music": "skills.yt_music",
    "open_youtube": "skills.web_opener",
    "open_google": "skills.web_opener",
    "location": "skills.location",
    "wikipedia_search": "skills.wikipedia_search",
    "shutdown": "skills.system_control",
    "exit": "skills.system_control"

    # Add more intent mappings as modules grow
}

def route_intent(intent: str, query: str):  
    """
    Routes the given intent to the appropriate skill module.
    Falls back to LLM if unknown or general.
    """
    try:
        if intent in INTENT_TO_SKILL:
            module_path = INTENT_TO_SKILL[intent]
            module = __import__(module_path, fromlist=['handle'])
            module.handle(query)
        else:
            # Fallback to LLM chat
            import skills.llm_chat as llm_chat
            llm_chat.handle(query)
    except Exception as e:
        print(f"⚠️ Error routing intent: {e}")
        speak("Sorry, I encountered an issue while processing that.")
