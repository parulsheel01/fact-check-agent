CLAIM_EXTRACTION_PROMPT = """
Extract factual claims from the following text.

Focus ONLY on:
- statistics
- percentages
- dates
- financial figures
- measurable statements
- company metrics

Return the claims as a Python list.

TEXT:
"""

VERIFICATION_PROMPT = """
You are a fact-checking AI.

Claim:
{claim}

Evidence:
{evidence}

Determine whether the claim is:
- Verified
- Inaccurate
- False

Also provide:
1. Explanation
2. Correct factual information

Return in this format:

Status:
Explanation:
Correct Fact:
"""