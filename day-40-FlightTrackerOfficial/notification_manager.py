from flight_data import FlightData
from smtplib import SMTP


class NotificationManager:
    def __init__(self, currency, email_user, password):
        self.min_dict = None
        self.flights_list = None
        self.clients = None
        self.currency = currency
        self.email_user = email_user
        self.password = password

    def check_flight(self, min_list: list, flights_list: list, client_list: list):
        self.min_dict = {min_dict.get("iataCode"): min_dict.get("lowestPrice") for min_dict in min_list}
        self.flights_list = flights_list
        cheaper_flights = self._values_to_send()
        self.clients = client_list
        messages = []
        for flight in cheaper_flights:
            msg = self._draft_message(flight)
            messages.append(msg)
        subject = "SUBJECT: Great Flight Deals!!!\n\n"
        if len(messages) > 0:
            self._send_emails(message=subject+"\n".join(messages), clients=client_list)

    def _draft_message(self, flight: FlightData):
        message = (
            f"FLight Deal Low price alert! Only {flight.price}{self.currency} to fly "
            f"from {flight.cityFrom}-{flight.flyFrom} to {flight.cityTo}"
            f"-{flight.flyTo}, from {flight.outbound_date.strftime('%Y-%m-%d')}"
            f" to {flight.inbound_date.strftime('%Y-%m-%d')} for {flight.total_nights} days.")
        if flight.stop_over is not None:
            message += f"There would be one stopover through {flight.stop_over}."
        return message

    def _send_emails(self, message: str, clients: list):
        for client in clients:
            with SMTP(host="smtp.gmail.com", port=587) as response:
                response.starttls()
                response.login(user=self.email_user, password=self.password)
                response.sendmail(from_addr=self.email_user, to_addrs=client, msg=message)
        print("Message Sent!")

    def _values_to_send(self):
        to_send = []
        for flight in self.flights_list:
            lowest_price_chosen = self.min_dict[flight.cityCodeTo]
            if lowest_price_chosen > flight.price:
                to_send.append(flight)
        return to_send
