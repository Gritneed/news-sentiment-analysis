import requests
from datetime import datetime, timedelta
import json

def fetch_news_articles(company_name, api_key, days_back=7):
    url = "https://newsapi.org/v2/everything"
    date_from = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')

    params = {
        'q': company_name,
        'from': date_from,
        'sortBy': 'publishedAt',
        'language': 'en',
        'apiKey': api_key
    }

    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    API_KEY = '19eeb291eb414644b2bfd2110f9c26ad'
    company_name = 'Tesla'
    result = fetch_news_articles(company_name, API_KEY)

    print(json.dumps(result, indent=4))