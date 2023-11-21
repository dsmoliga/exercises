from dataclasses import dataclass


@dataclass
class FlightData:
    price: int
    origin_city: str
    origin_airport: str
    destination_city: str
    destination_airport: str
    out_date: str
    return_date: str
