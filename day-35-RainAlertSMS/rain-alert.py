import datetime as dt
import os

import requests

from twilio.rest import Client

URL = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY_WEATHER = os.environ.get("OW_API")

ACCOUNT_SID = os.environ.get("T_AUTH_ID")
auth_token = os.environ.get("T_KEY")
client = Client(ACCOUNT_SID, auth_token)

PHONE_NUMER = os.environ.get("T_PHONE")
PSNL_PHONE_NUMBER = os.environ.get("PSNL_PHONE")

param = {
    "q": 'Zibello,Italy ',
    'appid': API_KEY_WEATHER,
    'cnt': 5
}

response = requests.get(url=URL, params=param)
response.raise_for_status()
data = response.json()

# {"time": iter_dict.get("dt_txt"), "rain": iter_dict.get("weather").get("main")}
rain_dict_list = [{"time": dt.datetime.strptime(iter_dict.get('dt_txt'), '%Y-%m-%d %H:%M:%S'),
                   "condition": iter_dict.get("weather")[0].get("main"),
                   "id": iter_dict.get("weather")[0].get("id")}
                  for iter_dict in data.get("list")]
print(rain_dict_list)


def check_rain(dict_list):
    for iter_dict in dict_list:
        if iter_dict.get("id") < 700:
            return True
    return False


def send_message():
    if check_rain(rain_dict_list):
        message = client.messages .create(
            body="Bring an Umbrella Today",
            from_=PHONE_NUMER,
            to=PSNL_PHONE_NUMBER
        )
        print(message.status)


send_message()
