import requests
import os
from dotenv import load_dotenv
from tools import web_search
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
import uvicorn

load_dotenv(override=True)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

app = FastAPI()

SYSTEM_PROMPT = """You are TechPulse, an expert AI agent specializing in:
- Latest AI and Machine Learning news and breakthroughs
- Startup and tech industry news, funding, and trends

Your behavior:
1. For any question about recent news or current events, you MUST use the [SEARCH] tag to search the web first.
2. To search, output exactly: [SEARCH] your search query here
3. After getting search results, give a clear and insightful answer.
4. If a question is unrelated to AI, ML, startups, or tech industry — politely decline.
5. Always be concise, sharp, and informative.
"""

conversation = [{"role": "system", "content": SYSTEM_PROMPT}]

def call_groq(messages):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 1024
    }
    response = requests.post(GROQ_URL, headers=headers, json=payload)
    data = response.json()
    if "choices" not in data:
        print("API Error:", data)
        return ""
    return data["choices"][0]["message"]["content"]

class Message(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
def index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/chat")
def chat(msg: Message):
    global conversation
    user_input = msg.text.strip()
    if not user_input:
        return JSONResponse({"reply": "Please ask something!"})

    conversation.append({"role": "user", "content": user_input})
    response = call_groq(conversation)

    if not response:
        return JSONResponse({"reply": "Something went wrong. Try again!"})

    if "[SEARCH]" in response:
        query = response.split("[SEARCH]")[-1].strip()
        print(f"🔍 Searching for: {query}")
        search_results = web_search(query)

        conversation.append({"role": "assistant", "content": response})
        conversation.append({
            "role": "user",
            "content": f"Here are the search results:\n{search_results}\nNow answer my original question."
        })

        final_response = call_groq(conversation)
        conversation.append({"role": "assistant", "content": final_response})
        return JSONResponse({"reply": final_response, "searched": True, "query": query})
    else:
        conversation.append({"role": "assistant", "content": response})
        return JSONResponse({"reply": response, "searched": False})

@app.post("/reset")
def reset():
    global conversation
    conversation = [{"role": "system", "content": SYSTEM_PROMPT}]
    return JSONResponse({"status": "reset"})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)