import requests
from prompts import SUMMARY_PROMPT

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:latest"

def summarize_text(text: str, max_words: int = 120) -> str:
    prompt = SUMMARY_PROMPT.format(
        text=text,
        max_words=max_words
    )

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()
    return response.json()["response"].strip()
