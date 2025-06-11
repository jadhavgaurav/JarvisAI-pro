import json
import random
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from core.config import INTENT_DATA_PATH, MODEL_PATH, VECTORIZER_PATH

# Global model/objects
model = None
vectorizer = None
intent_data = {}

def train_model():
    global model, vectorizer, intent_data

    with open(INTENT_DATA_PATH, "r", encoding="utf-8") as f:
        intent_data = json.load(f)

    texts, labels = [], []

    for item in intent_data:
        intent = item['intent']
        for example in item['examples']:
            texts.append(example.lower())
            labels.append(intent)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    model = MultinomialNB()
    model.fit(X, labels)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)
    print("✅ Intent classifier trained and saved.")

def load_model():
    global model, vectorizer
    if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)
    else:
        train_model()

def predict_intent(query: str) -> str:
    if not model or not vectorizer:
        load_model()

    X_test = vectorizer.transform([query.lower()])
    predicted = model.predict(X_test)[0]
    return predicted

def get_random_response(intent: str) -> str:
    for item in intent_data:
        if item['intent'] == intent and item.get('responses'):
            return random.choice(item['responses'])
    return "I'm not sure how to respond to that."
