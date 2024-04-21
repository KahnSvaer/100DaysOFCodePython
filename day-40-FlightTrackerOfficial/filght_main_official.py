import time
import os

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from customer import Customer


SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_HEADER = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}
SHEETY_ENDPOINT_PRICES = SHEETY_ENDPOINT + "/prices"
SHEETY_ENDPOINT_USERS = SHEETY_ENDPOINT + "/users"

KIWI_ENDPOINT = "https://api.tequila.kiwi.com"
KIWI_TOKEN = os.environ.get("KIWI_TOKEN")
KIWI_HEADER = {
    "apikey": KIWI_TOKEN
}

CURRENCY = 'GBP'

GMAIL_USER_ID = os.environ.get("GMAIL_USER_ID")
GMAIL_TOKEN = os.environ.get("GMAIL_TOKEN")

data_manager = DataManager(SHEETY_ENDPOINT_PRICES, SHEETY_HEADER)
customer = Customer(SHEETY_ENDPOINT_USERS, SHEETY_HEADER)


flight_search = FlightSearch(KIWI_ENDPOINT, KIWI_HEADER, CURRENCY)
notification_manager = NotificationManager(CURRENCY, email_user=GMAIL_USER_ID, password=GMAIL_TOKEN)

customer.sheety_fill_user()

sheet_data = data_manager.get_data().json().get("prices")
# city_codes = [flight_search.get_city_code(x.get("city")) for x in sheet_data]

# for i in range(len(city_code)):
#     sheet_data[i]["iataCode"] = city_code[i]
#     data_manager.update_data(sheet_data[i])

city_codes = [x.get("iataCode") for x in sheet_data]

flights = []
for city in city_codes:
    parsed = flight_search.get_cheap_flight(from_city="LON", to_city=city)
    if len(parsed.get("data")) == 0:
        parsed = flight_search.get_cheap_flight(from_city="LON", to_city=city, stop_overs=1)
    time.sleep(1)
    flight = parsed.get("data")[0]
    flight_info = FlightData(flight)
    flights.append(flight_info)

client_list = customer.get_emails()
notification_manager.check_flight(flights_list=flights, client_list=client_list, min_list=sheet_data)
