# 🧠 GenAI Market Researcher

A multi-agent Generative AI system that performs **market research, use-case generation, and resource discovery** for any company & industry using **Google Gemini** + **SerpAPI** + **Streamlit**.

👉 Live Demo: [GenAI Market Researcher](https://genai-market-researcher.streamlit.app/)

---

## 🚀 Overview

This project automates **end-to-end market research** using AI agents:

1. **Research Agent** – Collects company/industry information using web search.
2. **LLM Summarizer (Gemini)** – Summarizes offerings, focus areas, and trends.
3. **Use Case Agent** – Generates GenAI/LLM/ML use cases with impact, feasibility & data needs.
4. **Resource Agent** – Finds relevant **datasets, models, repos** (Kaggle, HuggingFace, GitHub).
5. **Pipeline Output** – Produces structured reports (`.md` + `.json`) with insights and resource links.
6. **Optional UI** – Streamlit app for interactive exploration.

---

## ✨ Features

- Multi-agent architecture (Research, Use-case, Resource agents).
- Powered by **Google Gemini** for LLM reasoning.
- **Web search integration** (SerpAPI or Serper).
- Auto-generated **reports & JSON outputs**.
- **Streamlit UI** for easy demo and interaction.
- Modular folder structure for easy extension.

---

## 📂 Folder Structure

```
genai-market-researcher/
├── README.md
├── .env.example
├── requirements.txt
├── run_pipeline.py              # Main CLI pipeline
├── agents/
│   ├── research_agent.py        # Web search + summarizer
│   ├── usecase_agent.py         # Use-case generator
│   └── resource_agent.py        # Resource finder
├── utils/
│   ├── llm.py                   # Gemini wrapper
│   └── io_utils.py              # I/O helpers
├── outputs/                     # Generated reports & JSON
│   └── demo/
├── web_app/
│   └── app.py                   # Streamlit app
└── reports/
    └── final_report_template.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repo

```bash
git clone https://github.com/mr-poojit/genai-market-researcher.git
cd genai-market-researcher
```

### 2. Create virtual environment

```bash
python -m venv myenv
source myenv/bin/activate      # Linux/Mac
myenv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key
SERPAPI_API_KEY=your_serpapi_api_key
```

- **Gemini API Key** → from [Google AI Studio](https://aistudio.google.com/).
- **SerpAPI API Key** → from [SerpAPI](https://serpapi.com/).  
  (Optional: you can replace with Serper.dev if needed.)

---

## ▶️ Running the Pipeline (CLI)

Run end-to-end pipeline for any company & industry:

```bash
python run_pipeline.py --company "Flipkart" --industry "ecommerce" --outdir outputs/demo_flipkart
```

This generates:

- `company_profile.md` – summarized company insights
- `use_cases.md` – AI/ML/GenAI use-cases
- `resources.md` – dataset/model/repo links
- `results.json` – structured output

---

## 🌐 Running the Streamlit App

```bash
streamlit run web_app/app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

👉 Deployed Demo: [GenAI Market Researcher](https://genai-market-researcher.streamlit.app/)

---

## 📊 Outputs

Example outputs for `Flipkart (ecommerce)`:

- **Company Profile** – Summary of offerings, focus areas, trends
- **Use Cases** – AI-powered recommendations like supply chain optimization, personalized CX, fraud detection
- **Resources** – Kaggle datasets, HuggingFace models, GitHub repos

All results are saved in `outputs/`.

---

## 📦 Deliverables

- ✅ Source Code
- ✅ Final Report (Markdown + Flowchart)
- ✅ Demo Video (run pipeline & UI)
- ✅ Streamlit Deployment (optional but done)

---

## 💡 Future Improvements

- Switch SerpAPI → Serper (free API)
- Improve strict JSON parsing for use-case outputs
- Add vector database (FAISS/Pinecone) to store research corpus
- Fine-tune UI with filters/search

---

## 👨‍💻 Author

Built by **Poojit Jagadeesh Nagaloti**

- 🌐 Portfolio: [My Portfolio](https://poojit-nagaloti.netlify.app/)
- 💻 GitHub: [My GitHub](https://github.com/mr-poojit)

---
