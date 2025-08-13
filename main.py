import requests

_OLLAMA_BASE = "http://localhost:11434"
_CHAT_ENDPOINT = "/api/chat"
MODEL_URL = _OLLAMA_BASE + _CHAT_ENDPOINT
MODEL = "gemma3:4b"
SYSTEM_PROMPT = "You are a concise, helpful assistant."

def call_model(prompt: str, model: str = MODEL, model_url: str = MODEL_URL, system_prompt: str = SYSTEM_PROMPT) -> str:
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        "stream": False
    }
    try:
        resp = requests.post(model_url, json=payload)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.HTTPError as e:
        print(e)
        exit(1)


def get_text_response(raw_response: dict):
    return raw_response.get("message", {}).get("content", "")

if __name__ == "__main__":
    prompt = "provide an example passphrase"
    raw_response = call_model(prompt)
    print(raw_response)
    print(get_text_response(raw_response))