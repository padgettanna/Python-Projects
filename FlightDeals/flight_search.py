import requests
import datetime

TEQUILA_ENDPOINT = "Your API"
TEQUILA_API_KEY = "Your API key"
TOMORROW = datetime.date.today() + datetime.timedelta(days=1)
TOMORROW_PLUS_6MONTHS = TOMORROW + datetime.timedelta(days=180)


class FlightSearch:

    def get_destination_code(self, city_name):
        header = {
            "apikey": TEQUILA_API_KEY
        }
        params = {
            "term": city_name,
            "location_types": "city",
        }
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"

        tequila_response = requests.get(url=location_endpoint, params=params, headers=header)
        tequila_data = tequila_response.json()["locations"]
        code = tequila_data[0]["code"]
        return code

    def flight_prices_search(self, iata_code):
        search_api = "Your API"
        header = {
            "apikey": TEQUILA_API_KEY
        }
        search_params = {
            "fly_from": "Origin aiti code",
            "fly_to": iata_code,
            "date_from": TOMORROW.strftime("%d/%m/%Y"),
            "date_to": TOMORROW_PLUS_6MONTHS.strftime("%d/%m/%Y"),
            "curr": "USD",
            "max_stopovers": 0,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1
        }

        search_response = requests.get(url=search_api, params=search_params, headers=header)
        try:
            search_data = search_response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {iata_code}.")
            return None

        price = search_data["price"]
        departure_city = search_data["cityFrom"]
        departure_iata = search_data["cityCodeFrom"]
        destination_city = search_data["cityTo"]
        destination_iata = search_data["cityCodeTo"]
        out_date = search_data["route"][0]["local_departure"].split("T")[0]
        in_date = search_data["route"][1]["local_departure"].split("T")[0]
        flight_data = {}
        flight_info = ["price", "departure_city", "departure_iata", "destination_city", "destination_iata", "out_date", "in_date"]
        for i in flight_info:
            flight_data[i] = eval(i)
        print(f"{destination_city}: ${price}")
        return flight_data

