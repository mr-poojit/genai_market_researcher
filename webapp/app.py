# web_app/app.py
import streamlit as st
import subprocess, os, json
from pathlib import Path

st.set_page_config(layout="wide", page_title="GenAI Market Researcher", page_icon="🔍")
st.title("Multi-Agent Market Researcher")

company = st.text_input("Company name", value=" ")
industry = st.text_input("Industry", value=" ")
run_btn = st.button("Run pipeline")

if run_btn:
    outdir = f"outputs/streamlit_{company.replace(' ','_')}"
    cmd = f"python run_pipeline.py --company \"{company}\" --industry \"{industry}\" --outdir {outdir}"
    with st.spinner("Running pipeline... this will call web search + LLM (requires API keys)"):
        st.text("Running: " + cmd)
        res = os.system(cmd)
    st.success("Pipeline executed. Showing results.")
    results_json = Path(outdir) / "results.json"
    if results_json.exists():
        data = json.loads(results_json.read_text())
        st.subheader("Use Case Titles")
        for t in data.get("titles", []):
            st.markdown(f"- **{t}**")
        st.subheader("Resources (first use case)")
        first = list(data.get("resources", {}).keys())[0]
        sites = data["resources"][first]
        for site, items in sites.items():
            st.markdown(f"**{site}**")
            for it in items[:5]:
                st.markdown(f"- [{it['title']}]({it['link']}) — {it.get('snippet','')}")
    else:
        st.error("No results.json found. Check logs.")
