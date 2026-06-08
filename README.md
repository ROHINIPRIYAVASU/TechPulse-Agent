# TechPulse Agent 🚀

An AI-powered tech news agent that specializes in **AI/ML breakthroughs** and **startup & tech industry news**. Built with pure Python, Groq LLM, and Tavily web search.

## Features
- 🤖 Powered by **Groq LLaMA 3.3 70B** — fast and free
- 🔍 Real-time **web search** via Tavily API
- 💬 Clean **chat UI** with search indicators
- 🧠 **Conversation memory** — context retained between messages
- 🚫 **Topic-focused** — politely declines off-topic questions

## Tech Stack
| Layer | Tool |
|-------|------|
| LLM | Groq (LLaMA 3.3 70B) |
| Web Search | Tavily API |
| Backend | FastAPI + Uvicorn |
| Frontend | HTML + CSS + JS |

## Setup & Run

1. Clone the repo
2. Create virtual environment and activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Create `.env` file with your keys:
GROQ_API_KEY=your_groq_key_here
TAVILY_API_KEY=your_tavily_key_here

5. Run: `python agent.py`
6. Open browser → `http://localhost:8080`

## Demo
> "What are the latest AI breakthroughs?"
> "What startups got funded this week?"
> "Tell me about OpenAI's latest news"

## Built by
Rohini Priyavasu — [GitHub](https://github.com/ROHINIPRIYAVASU)