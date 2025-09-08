# agents/research_agent.py
import os
from serpapi import GoogleSearch
from typing import List, Dict
from utils.llm import summarize_text
from dotenv import load_dotenv

load_dotenv() 

SERP_API_KEY = os.getenv("SERPAPI_API_KEY")

def web_search(query: str, num: int = 6) -> List[Dict]:
    if not SERP_API_KEY:
        raise EnvironmentError("SERPAPI_API_KEY not set")
    params = {
        "q": query,
        "num": num,
        "api_key": SERP_API_KEY,
        "engine": "google"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    items = results.get("organic_results") or []
    simplified = []
    for r in items:
        simplified.append({
            "title": r.get("title"),
            "snippet": r.get("snippet"),
            "link": r.get("link")
        })
    return simplified

def build_research_corpus(company: str, industry: str) -> str:
    queries = [
        f"{company} official site",
        f"{company} company profile",
        f"{company} products services {industry}",
        f"{industry} industry AI use cases",
        f"{company} annual report {industry} (if available)"
    ]
    paragraphs = []
    for q in queries:
        items = web_search(q, num=4)
        paragraphs.append(f"## Search query: {q}\n")
        for it in items:
            paragraphs.append(f"- {it['title']}\n  - {it['snippet']}\n  - {it['link']}\n")
    return "\n".join(paragraphs)

def research_company(company: str, industry: str) -> Dict:
    corpus = build_research_corpus(company, industry)
    # LLM summary: company profile, key offerings, strategic focus areas, opportunities
    prompt_extra = (
        "From the above search fragments, produce:\n"
        "1) Company profile (2-4 lines)\n"
        "2) Key offerings / products\n"
        "3) Strategic focus areas (ops, supply chain, CX, etc.)\n"
        "4) Top 5 industry trends relevant to this company\n"
        "Format: JSON with keys: profile, offerings, focus_areas, trends\n"
    )
    summary = summarize_text(corpus, prompt_extra=prompt_extra)
    # Because LLM returns free text, just return both corpus and summary
    return {"corpus": corpus, "summary": summary}
