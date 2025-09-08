# run_pipeline.py
import argparse, os, json
from datetime import datetime
from agents.research_agent import research_company
from agents.usecase_agent import generate_use_cases
from agents.resource_agent import collect_resources
from utils.io_utils import write_markdown, write_json, ensure_dir
from dotenv import load_dotenv

load_dotenv() 
def format_company_md(company, industry, research):
    header = f"# Research for {company} ({industry})\n\n"
    header += "## LLM Summary\n\n"
    header += research["summary"] + "\n\n"
    header += "## Raw corpus\n\n"
    header += research["corpus"][:10000] + "\n\n"  # truncate if long
    return header

def format_usecases_md(usecases_text):
    md = "# Generated Use Cases\n\n"
    md += "The raw LLM output (JSON-like). Please parse/inspect.\n\n"
    md += "```\n" + usecases_text + "\n```\n"
    return md

def format_resources_md(resources_dict):
    md = "# Resource Links\n\n"
    for uc, sites in resources_dict.items():
        md += f"## {uc}\n"
        for site, items in sites.items():
            md += f"### {site}\n"
            for it in items:
                md += f"- [{it['title']}]({it['link']}) — {it.get('snippet','')}\n"
        md += "\n"
    return md

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--company", required=True)
    parser.add_argument("--industry", required=True)
    parser.add_argument("--outdir", default=f"outputs/{datetime.now().strftime('%Y%m%d_%H%M%S')}")
    args = parser.parse_args()

    ensure_dir(args.outdir)

    print("1) Researching company and industry (web search + LLM)...")
    research = research_company(args.company, args.industry)
    md_company = format_company_md(args.company, args.industry, research)
    write_markdown(os.path.join(args.outdir, "company_profile.md"), md_company)
    print("Saved company_profile.md")

    print("2) Generating use cases with LLM...")
    usecases_text = generate_use_cases(research["summary"])
    write_markdown(os.path.join(args.outdir, "use_cases.md"), format_usecases_md(usecases_text))
    print("Saved use_cases.md")

    # Try to extract titles quickly by naive parsing of the JSON-like output
    # We attempt to find lines that look like '- title:' or JSON keys; if not, use fallback
    print("3) Collecting resources for use cases (Kaggle/HuggingFace/GitHub)...")
    # Very naive: look for quoted titles in the usecases_text
    import re
    titles = re.findall(r'"title"\s*:\s*"([^"]+)"', usecases_text)
    if not titles:
        # try to extract headings
        titles = re.findall(r'^\s*-\s*([^:][^\n]+)', usecases_text, flags=re.M)[:6]
    if not titles:
        titles = [f"{args.industry} ai use case {i}" for i in range(1,5)]
    resources = collect_resources(titles)
    write_markdown(os.path.join(args.outdir, "resources.md"), format_resources_md(resources))
    write_json(os.path.join(args.outdir, "results.json"), {"company": args.company, "industry": args.industry, "titles": titles, "resources": resources})
    print("Saved resources.md and results.json")
    print("Pipeline complete. Check folder:", args.outdir)

if __name__ == "__main__":
    main()
