# AI Fact-Checking Web App

## Overview

This project is an AI-powered Fact-Checking Web Application that automatically verifies factual claims from uploaded PDF documents.

The system extracts claims such as:
- statistics
- percentages
- dates
- measurable statements
- company metrics

It then cross-references those claims with live web search results and classifies them as:

- Verified
- Inaccurate
- False

---

## Features

- PDF Upload Interface
- Automated Claim Extraction
- Live Web Verification
- Fact Classification
- Streamlit-based UI
- Public Cloud Deployment

---

## Tech Stack

- Python
- Streamlit
- PyMuPDF
- spaCy
- Tavily Search API

---

## Project Structure

```bash
fact-check-agent/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── README.md
│
├── services/
│   ├── pdf_parser.py
│   ├── claim_extractor.py
│   ├── web_search.py
│   ├── verifier.py
│
└── utils/
    └── prompts.py