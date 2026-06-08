import requests, os
from dotenv import load_dotenv
load_dotenv()

headers = {
    "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
    "Content-Type": "application/json"
}

r = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers=headers,
    json={"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": "hi"}], "max_tokens": 10}
)
print(r.json())