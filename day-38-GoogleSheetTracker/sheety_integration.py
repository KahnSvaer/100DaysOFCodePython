import datetime
import os

import requests

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
AUTHORISATION_TOKEN = os.environ.get("AUTHORISATION_TOKEN")

header = {
    "Authorization": f"Bearer {AUTHORISATION_TOKEN}"
}


def add_row(exercise: str, duration, calories):
    user_param = {
        "workout": {
            "date": datetime.datetime.now().date().strftime("%d-%m-%y"),
            "time": datetime.datetime.now().time().strftime("%H:%M:%S"),
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=user_param, headers=header)
    response.raise_for_status()
