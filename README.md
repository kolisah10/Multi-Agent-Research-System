<div align="center">

# 🧠 ResearchMind

**Multi-agent AI research system that searches, scrapes, writes, and critiques — end to end.**

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-researchmind--koli.streamlit.app-ff6a00?style=for-the-badge)](https://researchmind-koli.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-🦜🔗-1C3C3C?style=flat-square)](https://www.langchain.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Orchestration-1C3C3C?style=flat-square)](https://www.langchain.com/langgraph)
[![Groq](https://img.shields.io/badge/Groq-Llama_3.3_70B-F55036?style=flat-square)](https://groq.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)

</div>

---

## Overview

**ResearchMind** takes a topic and turns it into a polished, source-backed research report — no manual searching or writing involved. Four specialized agents/chains each own one stage of the pipeline, handing off their output to the next:

| Step | Agent / Chain | Role |
|------|---------------|------|
| 1️⃣ | **Search Agent** | Queries the web via the Tavily Search API for recent, reliable sources |
| 2️⃣ | **Reader Agent** | Scrapes the most relevant source URL and extracts its full text |
| 3️⃣ | **Writer Chain** | Synthesizes everything into a structured report — intro, key findings, conclusion, sources |
| 4️⃣ | **Critic Chain** | Scores the report out of 10 and gives honest, constructive feedback |

```
Topic → 🔍 Search Agent → 📖 Reader Agent → ✍️ Writer Chain → 🧐 Critic Chain → Report + Feedback
```

Because every report is grounded in live web sources rather than the model's training data alone, and self-reviewed by a dedicated critic step, the output stays current and gets a built-in quality check.

## ✨ Features

- 🔎 Real-time web search via Tavily, not stale training data
- 📖 Automatic content extraction from live web pages
- ✍️ Structured, professional report generation
- 🧐 Built-in self-critique with a numeric score and specific feedback
- 🎨 Clean, branded Streamlit interface with live pipeline status
- ⬇️ One-click Markdown export of the final report

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| LLM inference | [Groq](https://groq.com/) — `llama-3.3-70b-versatile` |
| Agent orchestration | [LangChain](https://www.langchain.com/), [LangGraph](https://www.langchain.com/langgraph) |
| Web search | [Tavily Search API](https://tavily.com/) |
| Web scraping | BeautifulSoup, Requests |
| UI | [Streamlit](https://streamlit.io/) |
| Config | python-dotenv |

## 📁 Project Structure

```
ResearchMind/
├── agents.py          # Agent/chain definitions (search, reader, writer, critic)
├── tools.py           # web_search and scrape_url tool implementations
├── pipeline.py         # Orchestrates the 4-step research pipeline
├── app.py            # Streamlit UI
├── requirements.txt      # Python dependencies
└── .gitignore
```

## 🚀 Getting Started

**1. Clone the repo**
```bash
git clone https://github.com/kolisah10/Multi-Agent-Research-System.git
cd Multi-Agent-Research-System
```

**2. Create a virtual environment and install dependencies**
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows PowerShell
pip install -r requirements.txt
```

**3. Add your API keys**

Create a `.env` file in the project root:
```env
GROQ_API_KEY=your-groq-api-key
TAVILY_API_KEY=your-tavily-api-key
```

**4. Run it**

From the command line:
```bash
python pipeline.py
```

Or launch the Streamlit UI:
```bash
streamlit run app.py
```

## 🌐 Live Demo

**[researchmind-koli.streamlit.app →](https://researchmind-koli.streamlit.app)**

## 🗺️ Roadmap

- [ ] Stream live step-by-step progress in the UI instead of a single spinner
- [ ] Support multi-source scraping instead of a single top URL
- [ ] Add report history / session persistence

## 📄 License

MIT
