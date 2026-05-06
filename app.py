import streamlit as st
from dotenv import load_dotenv

from services.pdf_parser import extract_text_from_pdf
from services.claim_extractor import extract_claims
from services.web_search import search_claim
from services.verifier import verify_claim

load_dotenv()

st.set_page_config(page_title="Fact Check Agent")

st.title("AI Fact-Checking Agent")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    st.info("Extracting text from PDF...")

    text = extract_text_from_pdf(uploaded_file)

    st.success("PDF text extracted!")

    st.info("Extracting factual claims...")

    claims = extract_claims(text)

    st.write("### Claims Found")

    st.write(claims)

    results = []

    for claim in claims:

        st.info(f"Checking claim: {claim}")

        evidence = search_claim(claim)

        verdict = verify_claim(claim, evidence)

        results.append({
            "claim": claim,
            "verdict": verdict
        })

    st.write("## Fact Check Results")

    for result in results:

        st.subheader(result["claim"])

        st.write(result["verdict"])

        st.divider()