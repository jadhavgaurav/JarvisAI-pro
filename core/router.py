from core.speaker import speak
from core.intent_classifier import get_random_response

# Intent → skill mapping
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
    "exit": "skills.system_control",
    "open_app": "skills.system_control",
    "close_app": "skills.system_control",
    "restart": "skills.system_control",
    "sleep": "skills.system_control",
    "set_alarm": "skills.system_control",

}

def route_intent(intent: str, query: str):
    """
    Routes the given intent to the appropriate skill module.
    Falls back to LLM if unknown or general.
    """
    try:
        # ✅ Handle smalltalk directly with response
        if intent == "smalltalk":
            response = get_random_response(intent)
            speak(response)
            return

        # ✅ Route to skill module
        if intent in INTENT_TO_SKILL:
            module_path = INTENT_TO_SKILL[intent]
            module = __import__(module_path, fromlist=['handle'])
            module.handle(query)

        else:
            # ✅ Fallback to LLM
            import skills.llm_chat as llm_chat
            llm_chat.handle(query)

    except Exception as e:
        print(f"⚠️ Error routing intent: {e}")
        speak("Sorry, I encountered an issue while processing that.")
