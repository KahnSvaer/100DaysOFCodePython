import datetime
import requests


class FlightSearch:

    def __init__(self, endpoint: str, header: dict, currency: str):
        self.code_endpoint = f"{endpoint}/locations/query"
        self.search_endpoint = f"{endpoint}/v2/search"
        self.header = header
        self.currency = currency

    def get_city_code(self, city: str):
        json = {
            "term": city,
            "location_types": "city",
        }
        response = requests.get(url=self.code_endpoint, params=json, headers=self.header)
        response.raise_for_status()
        return response.json().get("locations")[0].get("code")

    def get_cheap_flight(self, from_city: str, to_city: str, stop_overs=0):
        json = {
            "fly_from": from_city,
            "fly_to": to_city,
            "date_from": (datetime.datetime.now().date()+datetime.timedelta(1)).strftime("%d/%m/%Y"),
            "date_to": (datetime.datetime.now().date()+datetime.timedelta(180)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "curr": self.currency,
            "max_stopovers": 2*stop_overs
        }
        response = requests.get(url=self.search_endpoint, params=json, headers=self.header)
        return response.json()
