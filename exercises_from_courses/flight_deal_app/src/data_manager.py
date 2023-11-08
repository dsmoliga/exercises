import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/0063bf2e9d93f64cecf2a9b4c82c9a58/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_flight_prices(self):
        self.response = requests.get(SHEETY_PRICES_ENDPOINT)
        self.prices_data = self.response.json()
        self.destination_data = self.prices_data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {"iataCode": city["iataCode"]}
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)
