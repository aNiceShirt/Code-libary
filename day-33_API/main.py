import requests
from datetime import datetime

MY_LAT = 56.158150
MY_LNG = 10.212030
FACTOR = 10

def is_ISS_overhead(MY_LAT=MY_LAT, MY_LNG=MY_LNG):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status() ## Uses requests module to output exceptions
    data = response.json() # all data
    iss_latitude = float(response.json()["iss_position"]["latitude"])
    iss_longitude = float(response.json()["iss_position"]["longitude"])
    iss_position = (iss_latitude, iss_longitude)
    # print("ISS position:", iss_position)  
    if MY_LAT - FACTOR <= iss_latitude <= MY_LAT + FACTOR and MY_LNG - FACTOR <= iss_longitude <= MY_LNG + FACTOR:
        print("is_overhead")
        return True
    else:
        return False


def is_dark():
    parameters = {"lat": MY_LAT,
                "lng": MY_LNG,
                "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    time_now = datetime.now()
    hour_now = time_now.hour
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if hour_now < sunrise and hour_now > sunset:
        return True
    else:
        return False


if is_ISS_overhead() and is_dark():
    print("look up")
else:
    print("wait")