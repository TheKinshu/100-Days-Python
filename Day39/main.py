#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager

dataManager = DataManager()

sheet_data = dataManager.getSheetyJson()

for index in range(len(sheet_data)):
    if sheet_data[index]["iataCode"] == "":
        id = sheet_data[index]['id']
        dataManager.updateSheety(id)
        