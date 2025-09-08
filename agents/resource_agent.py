# agents/resource_agent.py
import os
from serpapi import GoogleSearch
from typing import List, Dict
from urllib.parse import quote_plus

SERP_API_KEY = os.getenv("SERPAPI_API_KEY")

def search_resources_for_keyword(keyword: str, site_filter: str = None, num=5) -> List[Dict]:
    """
    site_filter examples: "kaggle.com", "huggingface.co", "github.com"
    """
    if not SERP_API_KEY:
        raise EnvironmentError("SERPAPI_API_KEY not set")
    q = f'{keyword} dataset'
    if site_filter:
        q = f"site:{site_filter} {keyword} dataset"
    params = {"q": q, "num": num, "api_key": SERP_API_KEY, "engine": "google"}
    res = GoogleSearch(params).get_dict()
    items = res.get("organic_results") or []
    out = []
    for it in items:
        out.append({
            "title": it.get("title"),
            "snippet": it.get("snippet"),
            "link": it.get("link")
        })
    return out

def collect_resources(use_case_titles: List[str]) -> Dict:
    results = {}
    for title in use_case_titles:
        results[title] = {
            "kaggle": search_resources_for_keyword(title, site_filter="kaggle.com", num=5),
            "huggingface": search_resources_for_keyword(title, site_filter="huggingface.co", num=4),
            "github": search_resources_for_keyword(title, site_filter="github.com", num=4)
        }
    return results
