import requests, datetime as dt
from requests.models import Response

# https://pixe.la/v1/users/kinshu/graphs/graph1.html

URL = "https://pixe.la/v1/users"
USERNAME = "kinshu"
TOKEN = "thisisatoken"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=URL, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{URL}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hour/s",
    "type": "float",
    "color": "sora"
}

headers ={
    "X-USER-TOKEN": TOKEN
}

GRAPH_VALUE_ENDPOINT = f"{GRAPH_ENDPOINT}/{graph_params['id']}"

today = dt.datetime(year=2021, month=4, day=9)

formateTime = today.strftime("%Y%m%d")

value_params = {
    "date": formateTime,
    "quantity": "1.5"
}

update_value_params = {
    "quantity": "5"
}

PUT_VALUE_ENDPOINT = f"{URL}/{USERNAME}/graphs/{graph_params['id']}/{formateTime}"

response = requests.post(url=PUT_VALUE_ENDPOINT, json=update_value_params, headers=headers)

print(response.text)