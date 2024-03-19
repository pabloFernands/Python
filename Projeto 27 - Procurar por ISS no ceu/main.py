import requests
from datetime import datetime
from tkinter import messagebox

MY_LAT = -22.9035
MY_LONG = -43.2096

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

#print(data["results"]["sunset"])
#print(sunset)

time_now = datetime.now().hour
#print(time_now)

if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_latitude <= MY_LONG + 5:
    if time_now >= sunset and time_now <= sunrise:
        messagebox.showinfo("Ele chegou!","Vá para a rua e olhe para cima!")
