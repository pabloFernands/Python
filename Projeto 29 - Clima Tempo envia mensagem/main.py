import json
import os
import requests
from twilio.rest import Client

#account_sid = ""
#auth_token = os.getenv("owm_auth_token")

latitude = -31.746611
longitude = -52.335388
API_KEY = os.getenv("OWM_API_KEY_TEST")
wheater_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

wheather_params = {
    "lat": latitude,
    "lon": longitude,
    "appid": API_KEY,
    "cnt": 4,
}

#response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}"
#                            f"&appid={API_KEY}")
#print(response.status_code)
#print(response.json())

response_second = requests.get(wheater_endpoint, params=wheather_params)
data_status = response_second.status_code
wheater_json = response_second.json()

rain = False
wheater_list = wheater_json["list"]

for item in wheater_list:
    wheater = item["weather"]
    for x in wheater:
        wheater_id = int(x["id"])
        #print(wheater_id)
        if wheater_id < 700:
            rain = True

if rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Vai chover! Pegue um guarda chuva.☂️",
        from_="+",
        to="+"
        )

print(message.status)
#print(wheater_list)
