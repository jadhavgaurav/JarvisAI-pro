from core.listener import listen
from core.speaker import speak
from core.intent_classifier import predict_intent, train_model
from core.router import route_intent

def run_jarvis(use_text_input=False):
    speak("Hello, I am Jarvis Pro. How can I assist you today?")

    while True:
        if use_text_input:
            query = input("📝 Type your command: ").strip().lower()
        else:
            query = listen()

        if query in ["", "none", None]:
            speak("Sorry, I didn't catch that.")
            continue

        # Predict intent
        intent = predict_intent(query)

        # Route to appropriate skill
        route_intent(intent, query)

        # Exit command is handled in router/system_control

if __name__ == "__main__":
    train_model()  # Only once if model not trained
    # ✅ Toggle voice or text input mode
    run_jarvis(use_text_input=True)
