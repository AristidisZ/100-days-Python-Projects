import requests

api_key = "32f20d3f292e61af1568c990df6cdaa9"
one_call = "https://api.openweathermap.org/data/3.0/onecall"
open_weather = "https://api.openweathermap.org/data/2.5/weather"
three_hours = "https://api.openweathermap.org/data/2.5/forecast"

MY_LAT = 40.66
MY_LONG = 22.89

TEST_LAT = -11.632240
TEST_LON = 27.460640

parameters = {
    "lat": TEST_LAT,
    "lon": TEST_LON,
    "appid": api_key
}

response = requests.get(three_hours, params=parameters)
response.raise_for_status()

data = response.json()
# print(data)
weather_data = data["list"][:3]
# print(len(weather_data))
will_rain = False

for i in weather_data:
    weather_id = i["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    print("take an umprella")

