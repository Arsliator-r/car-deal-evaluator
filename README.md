# 🚗 Pakistani Car Deal Evaluator

An AI-powered tool that helps Pakistani used car buyers make smarter purchasing decisions. Input a car listing and get an instant evaluation — verdict, red flags, questions to ask the seller, and negotiation advice — all grounded in real market context.

---

## The Problem

Pakistan's used car market is largely unregulated and opaque. Buyers — especially first-timers — have no reliable way to know whether an asking price is fair, what to watch out for in a listing, or how to negotiate effectively. Most end up overpaying or missing serious red flags.

---

## The Solution

This tool uses a locally-grounded LLM chain to evaluate any car listing against Pakistani market realities. It returns structured, actionable output rather than generic advice — built specifically for the Pakistani automotive context.

---

## Features

- **Deal Verdict** — Fair Deal, Good Deal, or Overpriced with reasoning
- **Red Flags** — Top concerns about the specific listing
- **Seller Questions** — What to ask before committing
- **Negotiation Advice** — Counter offer suggestion with reasoning
- **Clean UI** — Simple Streamlit interface, no technical knowledge required

---

## Tech Stack

| Layer | Technology |
|---|---|
| LLM Orchestration | LangChain |
| Model Provider | Groq API |
| Language Model | Qwen3 27B |
| Structured Output | Pydantic + `with_structured_output()` |
| Frontend | Streamlit |
| Language | Python 3.13 |

---

## Project Structure

```
car-deal-evaluator/
├── app.py            # Streamlit UI
├── chain.py          # LangChain logic
├── prompts.py        # Prompt templates and Pydantic schema
├── .env              # API keys (never committed)
├── .gitignore
└── requirements.txt
```

---

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/Arsliator-r/car-deal-evaluator.git
cd car-deal-evaluator
```

**2. Create and activate a virtual environment**
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up your API key**

Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key_here
```

Get a free API key at [console.groq.com](https://console.groq.com)

**5. Run the app**
```bash
streamlit run app.py
```

---

## Usage

1. Enter the car details — make, model, year, mileage, city, asking price
2. Add any description from the listing
3. Click **Evaluate This Deal**
4. Get your structured evaluation instantly

---

## Context & Background

This project is part of a broader series focused on the Pakistani automotive market. It builds on domain knowledge developed during my Final Year Project — **Smart Car Advisor** — a predictive pricing engine trained on 3,500+ real PakWheels listings that achieved 97.18% R² accuracy.

The goal of both projects is the same: bring data-driven decision making to a market that largely runs on gut feeling and information asymmetry.

---

## Roadmap

- [ ] Integrate real PakWheels listing data via RAG for grounded price comparisons
- [ ] Add model-year specific reliability scores
- [ ] Support image-based listing analysis
- [ ] Deploy as a public web tool

---

## Author

**Muhammad Arsalan**  
AI Engineer — Agentic Systems & LLM Applications  
[LinkedIn](https://www.linkedin.com/in/arsliator-r) · [GitHub](https://github.com/Arsliator-r)

---

## License

MIT License — free to use, modify, and distribute.
