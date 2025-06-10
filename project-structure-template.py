import os

folders = [
    "core", "skills", "rag_engine", "data", "db"
]

files = {
    "main.py": "",
    "requirements.txt": "",
    "README.md": "",
    "core/speaker.py": "",
    "core/listener.py": "",
    "core/intent_classifier.py": "",
    "core/router.py": "",
    "core/db_manager.py": "",
    "core/config.py": "",
    "skills/web_opener.py": "",
    "skills/wikipedia_search.py": "",
    "skills/jokes.py": "",
    "skills/time_date.py": "",
    "skills/location.py": "",
    "skills/yt_music.py": "",
    "skills/system_control.py": "",
    "skills/llm_chat.py": "",
    "rag_engine/embedder.py": "",
    "rag_engine/vectorstore.py": "",
    "rag_engine/retriever.py": "",
    "rag_engine/prompt_builder.py": "",
    "rag_engine/rag_pipeline.py": "",
    "data/intents.json": "[]",  # Placeholder
    "data/chat_memory.json": "[]",
    "data/logs.txt": ""
}

# os.makedirs("JarvisAI-Pro", exist_ok=True)
# os.chdir("JarvisAI-Pro")

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Project structure initialized.")
