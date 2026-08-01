# ResearchMind 🧠

A multi-agent AI research system that autonomously searches, scrapes, writes, and critiques research reports on any topic — with a Streamlit UI on top.

## Overview

ResearchMind orchestrates four specialized agents/chains, each handling one stage of the research process:

1. **Search Agent** — queries the web via the Tavily Search API to gather recent, reliable sources on a topic.
2. **Reader Agent** — scrapes the most relevant source URL and extracts its full text content using BeautifulSoup.
3. **Writer Chain** — synthesizes the search results and scraped content into a structured research report (introduction, key findings, conclusion, sources).
4. **Critic Chain** — reviews the report, scores it out of 10, and gives constructive feedback (strengths, areas to improve, verdict).

The agents are built with **LangChain** and **LangGraph**, powered by **Groq** (`openai/gpt-oss-120b`), and wrapped in a **Streamlit** interface for interactive use.

## Tech Stack

- **LLM inference:** Groq
- **Agent orchestration:** LangChain, LangGraph
- **Web search:** Tavily Search API
- **Web scraping:** BeautifulSoup, Requests
- **UI:** Streamlit
- **Config:** python-dotenv

## Project Structure

```
├── agents.py         # Agent/chain definitions (search, reader, writer, critic)
├── tools.py           # web_search and scrape_url tool implementations
├── pipeline.py         # Orchestrates the 4-step research pipeline
├── app.py            # Streamlit UI
├── requirements.txt      # Python dependencies
└── .gitignore
```

## Setup

1. **Clone the repo**
  ```bash
  git clone https://github.com/kolisah10/Multi-Agent-Research-System.git
  cd Multi-Agent-Research-System
  ```

2. **Create a virtual environment and install dependencies**
  ```bash
  python -m venv .venv
  .venv\Scripts\Activate.ps1   # Windows PowerShell
  pip install -r requirements.txt
  ```

3. **Add your API keys**
  Create a `.env` file in the project root:
  ```
  GROQ_API_KEY=your-groq-api-key
  TAVILY_API_KEY=your-tavily-api-key
  ```

4. **Run the pipeline from the command line**
  ```bash
  python pipeline.py
  ```

5. **Or launch the Streamlit UI**
  ```bash
  streamlit run app.py
  ```

## Live Demo

[Add your Streamlit Cloud URL here once deployed]

## How It Works

Given a research topic, the pipeline runs sequentially:

```
Topic → Search Agent → Reader Agent → Writer Chain → Critic Chain → Final Report + Feedback
```

Each stage's output feeds into the next, so the final report is grounded in real, current web sources rather than the LLM's training data alone — and the critic step adds a self-evaluation layer for report quality.

## License

MIT
