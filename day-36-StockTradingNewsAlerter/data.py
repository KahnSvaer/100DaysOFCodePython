import json
import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

URL = "https://www.alphavantage.co/query"
AV_API_KEY = os.environ.get("AV_API_KEY")
STORAGE_DUMP = 'stock_data.json'

PARAM = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": AV_API_KEY
}


def update_file():
    response = requests.get(URL, params=PARAM)
    response.raise_for_status()
    with open(STORAGE_DUMP, mode="w") as file:
        json.dump(response.json(), file, indent=4)  # to avoid unnecessary api calls
        print("File Updated")
    return read_file()


def read_file():
    try:
        with open(STORAGE_DUMP) as file:
            api_data = json.load(file)
    except FileNotFoundError:
        api_data = update_file()
    return api_data

