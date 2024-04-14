import datetime
from twilio.rest import Client


class NotificationManager:
    def __init__(self, client: Client, twilio_num: str, psnl_num: str):
        self.client = client
        self.twilio_num = twilio_num
        self.psnl_num = psnl_num
        self.min_dict = None
        self.flight_search_result = None
        self.currency = None

    def check_flight(self, min_list: list, flight_search_result: dict):
        self.min_dict = {min_dict.get("city"): min_dict.get("lowestPrice") for min_dict in min_list}
        self.flight_search_result = flight_search_result.get("data")
        self.currency = flight_search_result.get("currency")
        cheaper_flights = self.values_to_send()
        for iterdict in cheaper_flights:
            self.parse_dict(iterdict)

    def parse_dict(self, dict_message: dict):
        outbound_date = datetime.datetime.strptime(dict_message.get('local_departure').split('T')[0], "%Y-%m-%d")
        total_nights = int(dict_message.get('nightsInDest'))
        print(total_nights)
        inbound_date = outbound_date + datetime.timedelta(total_nights)
        message = (f"Low price alert! Only {round(dict_message.get('price'))}{self.currency} to fly "
                   f"from {dict_message.get('cityFrom')}-{dict_message.get('flyFrom')} to {dict_message.get('cityTo')}"
                   f"-{dict_message.get('flyTo')}, from {outbound_date.strftime("%Y-%m-%d")}"
                   f" to {inbound_date.strftime("%Y-%m-%d")}.")
        self._send_message(message)

    def _send_message(self, message: str):
        self.client.messages.create(
            body=message,
            from_=self.twilio_num,
            to=self.psnl_num
        )

    def values_to_send(self):
        to_send = []
        for num in self.flight_search_result:
            lowest_price_chosen = self.min_dict[num.get("cityTo")]
            if lowest_price_chosen > num.get("price"):
                to_send.append(num)
        return to_send
