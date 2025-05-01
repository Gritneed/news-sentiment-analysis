import json
from datetime import datetime, timedelta
from typing import Any, Dict

import requests


def fetch_news_articles(
    company_name: str, api_key: str, days_back: int = 7
) -> Dict[str, Any]:
    """
    Fetch recent news articles related to a given company using NewsAPI.

    Args:
        company_name (str): Name of the company to search for.
        api_key (str): NewsAPI authentication key.
        days_back (int): Number of past days to include in the search.

    Returns:
        dict: JSON response containing articles.
    """
    url = "https://newsapi.org/v2/everything"
    date_from = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")

    params = {
        "q": company_name,
        "from": date_from,
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": api_key,
    }

    response = requests.get(url, params=params)
    return response.json()


if __name__ == "__main__":
    # Example test call to fetch articles
    API_KEY = "your_api_key_here"  # Replace with your own API key
    company_name = "Tesla"
    result = fetch_news_articles(company_name, API_KEY)

    print(json.dumps(result, indent=4))
