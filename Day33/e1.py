import requests
from requests.models import Response

MY_LAT = 43.653225
MY_LONG = -79.383186

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# print(data['iss_position'])

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
print(data)