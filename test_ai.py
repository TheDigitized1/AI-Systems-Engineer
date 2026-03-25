import os
import requests

API_KEY = os.getenv("AI_API_KEY")

def call_model(prompt: str) -> str:
    # Placeholder — we’ll wire this up once you choose a model provider
    return "AI response placeholder"

if __name__ == "__main__":
    print(call_model("Hello AI"))
