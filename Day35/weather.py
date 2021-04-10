import requests, os
from twilio.rest import Client


MYLONG = -79.383186
MYLAT = 43.653225
URL = "https://api.openweathermap.org/data/2.5/onecall"

api_key = os.getenv('WEATHER_API')
twilio_account_sid = os.getenv('TWILIO_SID')
twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
my_number = os.getenv('MY_NUMBER')

parameters = {
    "lat": MYLAT,
    "lon": MYLONG,
    "exclude": "current,minutely,daily",
    "appid": api_key 
}

response =  requests.get(url=URL, params=parameters)
response.raise_for_status()

weatherData = response.json()

weatherSlice = weatherData['hourly'][:12]

willRain = False

for hourData in weatherSlice:
    condition_code = hourData["weather"][0]['id']
    if int(condition_code) < 700:
        willRain = True
        
if willRain:
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages \
        .create(
            body='Its going to rain today. Remember to bring an umbrella',
            from_='+13472271948',
            to=f'{my_number}'
        )
    print(message.status)