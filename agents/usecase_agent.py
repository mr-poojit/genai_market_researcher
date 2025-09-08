# agents/usecase_agent.py
from utils.llm import call_chat
from typing import List, Dict

def generate_use_cases(company_summary_text: str, num_cases: int = 6):
    system = {"role": "system", "content": "You are an expert AI product manager and solution architect."}
    user = {
        "role": "user",
        "content": (
            "Given the following company and industry summary, propose top GenAI/LLM/ML use cases.\n\n"
            "For each use case provide:\n"
            "- title\n"
            "- description (1-2 sentences)\n"
            "- business impact\n"
            "- required data sources\n"
            "- feasibility (Low/Medium/High)\n\n"
            f"Company/Industry summary:\n{company_summary_text}\n\n"
            "Output as JSON array."
        )
    }
    out = call_chat([system, user], max_tokens=1200)
    return out
