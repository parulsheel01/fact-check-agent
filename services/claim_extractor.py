import re
import spacy

nlp = spacy.load("en_core_web_sm")


def extract_claims(text):

    claims = []

    sentences = text.split(".")

    pattern = r'\d+%|\$[\d,]+|\d+\s?(million|billion|trillion)|\d{4}'

    for sentence in sentences:

        if re.search(pattern, sentence, re.IGNORECASE):

            cleaned = sentence.strip()

            if len(cleaned) > 20:
                claims.append(cleaned)

    return list(set(claims))