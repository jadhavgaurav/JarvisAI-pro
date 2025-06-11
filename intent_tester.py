from core.intent_classifier import train_model, predict_intent

train_model()
print(predict_intent("set alarm for 7 AM"))
print(predict_intent("how is the weather today?"))