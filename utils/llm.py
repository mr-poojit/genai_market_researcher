# utils/llm.py
import os
import google.generativeai as genai
from typing import List, Dict

GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

def init_gemini():
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise EnvironmentError("GEMINI_API_KEY not set in environment")
    genai.configure(api_key=key)

def call_chat(messages: List[Dict], max_tokens=800, temperature=0.2, model=None):
    """
    messages: list of {"role": "system"/"user"/"assistant", "content": "..."}
    We'll concatenate into a single prompt for Gemini.
    """
    init_gemini()
    model = model or GEMINI_MODEL
    prompt = ""
    for m in messages:
        role = m["role"].upper()
        prompt += f"{role}: {m['content']}\n"
    response = genai.GenerativeModel(model).generate_content(
        prompt,
        generation_config={
            "temperature": temperature,
            "max_output_tokens": max_tokens,
        }
    )
    return response.text.strip()

def summarize_text(text: str, prompt_extra: str = "") -> str:
    messages = [
        {"role": "system", "content": "You are an expert AI consultant who writes crisp summaries."},
        {"role": "user", "content": f"Summarize the following text concisely into bullet points (3-6):\n\n{text}\n\n{prompt_extra}"}
    ]
    return call_chat(messages)
