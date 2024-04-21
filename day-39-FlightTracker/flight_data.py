import datetime


class FlightData:
    def __init__(self, flight_info: dict):
        self.flyFrom = flight_info.get("flyFrom")
        self.flyTo = flight_info.get("flyTo")
        self.cityFrom = flight_info.get("cityFrom")
        self.cityTo = flight_info.get("cityTo")
        self.price = round(flight_info.get('price'))

        self.outbound_date = datetime.datetime.strptime(flight_info.get('local_departure').split('T')[0], "%Y-%m-%d")
        self.total_nights = int(flight_info.get('nightsInDest'))
        self.inbound_date = self.outbound_date + datetime.timedelta(self.total_nights)
