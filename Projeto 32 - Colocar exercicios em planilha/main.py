import requests
from datetime import datetime

nutri_header = {
    "x-app-id": "4848bf84",
    "x-app-key": "180caf93d37f5e78b6e19316c7afc833",
}

nutri_body = {
    "query": input("What exercise and time spent in minutes?")
}

nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
response_nutri = requests.post(url=nutri_endpoint, json=nutri_body, headers=nutri_header)
response_nutri = response_nutri.json()

user_input = response_nutri["exercises"][0]["user_input"]
user_duration = response_nutri["exercises"][0]["duration_min"]
user_calories = response_nutri["exercises"][0]["nf_calories"]
print(response_nutri)

#print(user_input)

today = datetime.now()
date = today.strftime(f"%d/%m/%Y")
hour = today.strftime("%H:%M:%S")


sheety_body = {
    "workout": {
        "date": date,
        "time": hour,
        "exercise": user_input,
        "duration": user_duration,
        "calories": user_calories,
    }
}


sheety_endpoint = "https://api.sheety.co/668082ab5b07946d3584554d2eec9f79/cópiaDeMyWorkoutsEstudo/workouts"
sheety_response = requests.post(url=sheety_endpoint, json=sheety_body)

print(sheety_response.text)
