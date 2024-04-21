from twilio.rest import Client
from flight_data import FlightData


class NotificationManager:
    def __init__(self, client: Client, twilio_num: str, psnl_num: str, currency):
        self.client = client
        self.twilio_num = twilio_num
        self.psnl_num = psnl_num
        self.min_dict = None
        self.flights_list = None
        self.currency = currency

    def check_flight(self, min_list: list, flights_list: list):
        self.min_dict = {min_dict.get("city"): min_dict.get("lowestPrice") for min_dict in min_list}
        self.flights_list = flights_list
        cheaper_flights = self.values_to_send()
        for iterdict in cheaper_flights:
            self.parse_dict(iterdict)

    def parse_dict(self, flight: FlightData):
        message = (f"Low price alert! Only {flight.price}{self.currency} to fly "
                   f"from {flight.cityFrom}-{flight.flyFrom} to {flight.cityTo}"
                   f"-{flight.flyTo}, from {flight.outbound_date.strftime('%Y-%m-%d')}"
                   f" to {flight.inbound_date.strftime('%Y-%m-%d')} for {flight.total_nights} days.")
        self._send_message(message)

    def _send_message(self, message: str):
        self.client.messages.create(
            body=message,
            from_=self.twilio_num,
            to=self.psnl_num
        )

    def values_to_send(self):
        to_send = []
        for flight in self.flights_list:
            lowest_price_chosen = self.min_dict[flight.cityTo]
            if lowest_price_chosen > flight.price:
                to_send.append(flight)
        return to_send
