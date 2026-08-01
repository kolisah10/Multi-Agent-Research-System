from langchain.tools import tool
import requests

from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
from rich import print
load_dotenv()

tavily=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query:str) ->str:
    """Search the web for recent and reliable information on a topic. Returns Titles,URLs and snippets."""
    results=tavily.search(query=query,max_results=5)
    
    out=[]
    for r in results["results"]:
        out.append(
            f"Title:{r['title']}\nURL:{r["url"]}\nSnippet:{r['content'][:300]}\n"
        )

    return "\n----\n".join(out) #ek list hai with multiple strings to wo join ho jaati hai

@tool
def scrape_url(url:str) -> str:
    """Scrape the content of a webpage given its URL. Returns the text content of the page."""
    try:
        resp = requests.get(url,timeout=8,headers={"User-Agent": "Mozilla/5.0"})
    
        soup = BeautifulSoup(resp.text, 'html.parser')
        for tag in soup(["script", "style","nav","footer"]):
            tag.decompose()  # Remove script and style elements
        return soup.get_text(separator=' ', strip=True)[:3000]
        
    except Exception as e:
        return f"Could not scrape the URL: {str(e)}"

