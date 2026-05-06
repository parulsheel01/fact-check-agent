def verify_claim(claim, evidence):

    claim_lower = claim.lower()
    evidence_lower = evidence.lower()

    matched_words = 0

    # Compare important words from claim with evidence
    for word in claim_lower.split():

        if len(word) > 4 and word in evidence_lower:
            matched_words += 1

    # Simple verification logic
    if matched_words > 5:
        verdict = "Verified"

    elif matched_words > 2:
        verdict = "Inaccurate"

    else:
        verdict = "False"

    result = f"""
Status: {verdict}

Explanation:
The system compared the uploaded claim with live web evidence gathered from online sources.

Correct Fact:
Please review the extracted evidence and URLs for the most up-to-date factual information.
"""

    return result