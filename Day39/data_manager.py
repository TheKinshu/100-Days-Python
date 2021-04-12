from pprint import pprint
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.URL = "https://api.sheety.co/533188763ceae6a22e3076b8fc223fd1/flightDeals/prices"
        self.response = requests.get(url=self.URL)
        self.response.raise_for_status()

    def getSheetyJson(self):
        return self.response.json()["prices"]

    def updateSheety(self, index):
        parameters = {
            "price" : {
               "iataCode": "TESTING" 
            }
        }
        newURL = f"{self.URL}/{index}"
        respoonse = requests.put(url=newURL, json=parameters)
        respoonse.raise_for_status()

