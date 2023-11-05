import requests as requests
import os
from twilio.rest import Client



auth_token = os.environ["Auth_Token"]  #Your API Token
print(auth_token)
Twilo_token = os.environ["Twilo_Token"] #Your API Token
print(Twilo_token)
account_sid = 'AC432f71b34a0a62d27eba4f10eded9a99'
client = Client(account_sid, Twilo_token)



is_rain=False


import html
parameter={
    "location":(26.605200,75.946297),
    "apikey":auth_token

}
response=requests.get(url='https://api.tomorrow.io/v4/weather/forecast',params=parameter)


def get_weather_description(weather_code):
    global is_rain
    weather_codes = {
        1000: "Clear sky",
        1001: "Partly cloudy",
        1002: "Scattered clouds",
        1003: "Broken clouds",
        1004: "Overcast",
        1005: "Foggy",
        1006: "Hazy",
        1007: "Mist",
        1008: "Light drizzle",
        1009: "Light rain",
        1010: "Rain",
        1011: "Heavy rain",
        1012: "Light snow",
        1013: "Snow",
        1014: "Heavy snow",
        1015: "Sleet",
        1016: "Freezing rain",
        1017: "Thunderstorm",
        1018: "Tornado",
        # Add more weather codes and descriptions as needed
    }

    # Check if the provided weather code exists in the dictionary
    if weather_code in weather_codes:
        if 1008<weather_code<1017:
            is_rain=True
        return weather_codes[weather_code]
    elif 1100 <= weather_code < 1200:
        return "Unknown weather code"
    else:
        return "Invalid weather code"


# Example usage:
weather_code = 1000  # Replace with the desired weather code
description = get_weather_description(weather_code)
print(f"Weather Description: {description}")
for i in range(12):
    data=response.json()['timelines']['hourly'][i]['values']['weatherCode']
    print(data)
    print(get_weather_description(data))


if is_rain:
    msg=f"There Might be Chances of Rain⛈️ Today So Bring Umbrella ☔ Today!!! "
    message = client.messages.create(
      from_='+13345106299',
      body=msg,
      to='+91xxxxxxxxx'
    )
