import os, requests
from datetime import datetime as dt

today = dt.now().date()

NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/533188763ceae6a22e3076b8fc223fd1/workoutTracking/workouts"

exercise_text = input("Tell me which excerises you did: ")

# 
nutritionix_parameters = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 6.7,
    "height_cm": 183,
    "age": 24
}

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}

excerise_response = requests.post(exercise_endpoint, json=nutritionix_parameters, headers=headers)
excerise_response.raise_for_status()
excerise_datas = excerise_response.json()["exercises"]

for excerise_data in excerise_datas:
    excerise_type = str(excerise_data['user_input']).title()
    excerise_duration = excerise_data["duration_min"]
    excerise_calories = excerise_data["nf_calories"]
    #
    workout_pararms = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": dt.now().time().strftime("%H:%M:%S"),
            "exercise": excerise_type,
            "duration": excerise_duration,
            "calories": excerise_calories
        }
    }

    
    headers = {
        "Authorization": os.getenv("sheety_token")
    }
    sheety_response = requests.post(sheety_endpoint, json=workout_pararms, headers=headers)
    sheety_response.raise_for_status()
    print(sheety_response.text)