from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()

if sheet_data[0]["iataCode"] == "":
    
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
print(sheet_data)
for row in sheet_data:
    flight_info = flight_search.flight_prices_search(row["iataCode"])
    if flight_info["price"] < row["lowestPrice"]:
        text = f"Low price alert! Only ${flight_info['price']} to fly from {flight_info['departure_city']}-{flight_info['departure_iata']} to {flight_info['destination_city']}-{flight_info['destination_iata']},from {flight_info['out_date']} to {flight_info['in_date']}."
        notification_manager.send_message(text)
