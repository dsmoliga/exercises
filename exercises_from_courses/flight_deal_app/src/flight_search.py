import requests
from src.flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_HEADER = {
    "apikey": "mX2_zixGwxWf1M0qE8LF-ijbP6N7BFC5"
}


class FlightSearch:
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = TEQUILA_HEADER

        query = {
            "term": city_name,
            "location_types": "city"
        }

        try:
            response = requests.get(
                location_endpoint, headers=headers, params=query)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Connection error: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Unexpected error: {err}")

        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = TEQUILA_HEADER

        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "PLN"
        }

        try:
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Connection error: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Unexpected error: {err}")

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
