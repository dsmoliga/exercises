import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/0063bf2e9d93f64cecf2a9b4c82c9a58/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_flight_prices(self):
        try:
            self.response = requests.get(SHEETY_PRICES_ENDPOINT)
            self.response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Connection error: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Unexpected error: {err}")

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
