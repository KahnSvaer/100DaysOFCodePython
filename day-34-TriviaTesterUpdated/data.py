import requests

URL = "https://opentdb.com/api.php"

params = {
    "type": "boolean",
    "amount": 10,
    "category": 31,
}

response = requests.get(url=URL, params=params)
response.raise_for_status()

question_data = response.json().get("results")