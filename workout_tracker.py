import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
TOKEN = os.environ["TOKEN"]

GENDER = "your gender"
AGE = YOUR AGE
HEIGHT_CM = YOUR HEIGHT
WEIGHT_KG = YOUR WEIGHT

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ["sheety_endpoint"]

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

exercise_text = input("What exercise did you do? ")

params = {
 "query": exercise_text,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE
}

response = requests.post(url=nutritionix_endpoint, json=params, headers=header)
result = response.json()
print(result)

today = datetime.now()

sheet_header = {
    "Authorization": TOKEN
}

for exercise in result["exercises"]:
    workout_inputs = {
        "sheet1": {
            "date": today.strftime("%x"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(url=sheety_endpoint, json=workout_inputs, headers=sheet_header)
    print(sheet_response.text)
