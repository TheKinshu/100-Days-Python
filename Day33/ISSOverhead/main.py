import requests
from datetime import datetime
import smtplib, time

MY_LAT = 43.653225
MY_LONG = -79.383186
my_email = "kelvc.app@gmail.com"
password = "jhljkmlnwhsybpkx"

def isISSOverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT +5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    else:
        return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if isISSOverhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Creating a secure connection
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=my_email, 
                msg=f"Subject:Look up\n\nThe ISS is above you in the sky"
        )
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



