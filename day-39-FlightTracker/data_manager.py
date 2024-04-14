import requests


class DataManager:
    def __init__(self, endpoint: str, header: dict):
        self.endpoint = endpoint
        self.header = header

    def get_data(self):
        response = requests.get(url=self.endpoint, headers=self.header)
        response.raise_for_status()
        return response

    def update_data(self, json: dict):
        data_id = json.get("id")
        update_endpoint = f"{self.endpoint}/{data_id}"
        update_json = {
            "price": {"city": json.get("city"),
                      "iataCode": json.get("iataCode"),
                      "lowestPrice": json.get("lowestPrice")}
        }
        response = requests.put(url=update_endpoint, headers=self.header, json=update_json)

        response.raise_for_status()
