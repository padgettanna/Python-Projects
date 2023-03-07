import requests

SHEETY_ENDPOINT = "https://api.sheety.co/b31e058def071dbf322682ba89550db1/flightDeals/prices"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheet_response = requests.get(url=SHEETY_ENDPOINT)
        sheet_data = sheet_response.json()
        self.destination_data = sheet_data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
