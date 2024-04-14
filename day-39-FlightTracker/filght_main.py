from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch

from twilio.rest import Client
import os

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_HEADER = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

KIWI_ENDPOINT = "https://api.tequila.kiwi.com"
KIWI_TOKEN = os.environ.get("KIWI_TOKEN")
KIWI_HEADER = {
    "apikey": KIWI_TOKEN
}

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
client = Client(TWILIO_SID, TWILIO_TOKEN)

TWILIO_PHONE_NUMER = os.environ.get("TWILIO_PHONE_NUMER")
PSNL_PHONE_NUMBER = os.environ.get("PSNL_PHONE_NUMBER")


data_manager = DataManager(SHEETY_ENDPOINT, SHEETY_HEADER)
flight_search = FlightSearch(KIWI_ENDPOINT, KIWI_HEADER)
notification_manager = NotificationManager(client, TWILIO_PHONE_NUMER, PSNL_PHONE_NUMBER)

sheet_data = data_manager.get_data().json().get("prices")
city_code = [flight_search.get_city_code(x.get("city")) for x in sheet_data]

# for i in range(len(city_code)):
#     sheet_data[i]["iataCode"] = city_code[i]
#     data_manager.update_data(sheet_data[i])

parsed = flight_search.get_cheap_flight(from_city="London", city_code_list=city_code)
notification_manager.check_flight(flight_search_result=parsed, min_list=sheet_data)
