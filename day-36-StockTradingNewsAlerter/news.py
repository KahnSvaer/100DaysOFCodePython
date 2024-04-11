import requests
import os

NEWS_API_URL = "https://newsapi.org/v2/top-headlines"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")


def get_news(page_size: int) -> list:
    param = {
        "apiKey": NEWS_API_KEY,
        "q": "tesla",
        "pageSize": page_size
    }
    response = requests.get(NEWS_API_URL, params=param)
    response.raise_for_status()
    return response.json().get("articles")
