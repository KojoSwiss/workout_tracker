import os
import requests
from datetime import datetime

today = datetime.now()
date_today = today.strftime("%d/%m/%Y")
time_now = today.strftime("%X")

my_username = os.environ["MY_USERNAME"]
my_password = os.environ["MY_PASSWORD"]

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/030c15a7e6cf42aefb7c29f533ff9b65/workoutTracking/workouts"

exercise = input("Which exercise did you do?")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_parameters = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 173,
    "age": 34
}

response = requests.post(url=exercise_endpoint, json=exercise_parameters, headers=headers)
exercise_data = response.json()

for exercise in exercise_data["exercises"]:
    sheet_parameters = {
        "workout": {
            "date": date_today,
            "time": time_now,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

# No Authentication
sheety_response = requests.post(url=sheety_endpoint, json=sheet_parameters)

# #Basic Authentication
# sheety_response = requests.post(url=sheety_endpoint, json=sheet_parameters, auth=(my_username, my_password))
#
#
# #Bearer Token Authentication
# bearer_headers = {
# "Authorization": "Bearer YOUR_TOKEN"
# }
# sheety_response = requests.post(
#     url=sheety_endpoint,
#     json=sheet_parameters,
#     headers=bearer_headers
# )