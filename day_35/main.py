import requests
from twilio.rest import Client
import os

# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "841549751a0bd3dbda6668f7a4a6c2a8"

account_sid = 'AC33aa47f1e8756079d080312ea0bb2fbd'
auth_token = "1fe425f6239dbff53ebabf4e728198c2"

weather_params = {
    "lat": 21.145800,
    "lon": 79.088158,
    "appid": api_key,
    "cnt": 4,
    }

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()


will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Your appointment is coming up on July 21 at 3PM',
        to='whatsapp:+254708318239'
    )

    print(message.status)
    # message = client.messages.create(
    #     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    #     from_="+18149073398",
    #     to="+254708318239",
    # )
    # print(message.status)




# MY_LAT = -1.171850
# MY_LNG = 36.842000
#
#
# response = requests.get(url="https://api.openweathermap.org/data/2.5/weather?lat=-1.171850&lon=36.842000&appid"
#                             "=841549751a0bd3dbda6668f7a4a6c2a8")
# response.raise_for_status()
# data = response.json()
# print(data)
