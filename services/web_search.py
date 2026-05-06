from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def search_claim(claim):

    response = client.search(
        query=claim,
        search_depth="advanced",
        max_results=5
    )

    results = response.get("results", [])

    evidence = ""

    for result in results:

        evidence += f"""
Title: {result.get('title')}

Content: {result.get('content')}

URL: {result.get('url')}

"""

    return evidence