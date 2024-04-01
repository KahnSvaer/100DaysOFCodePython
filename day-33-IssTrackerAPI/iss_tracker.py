import requests
import datetime as dt
import smtplib
import time

LAT = 28.64
LONG = 77.37
ALLOWED_DIFFERENCE = 5
TIMER = 60

USERNAME = ""
PASSWORD = ""

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # Automatic exception raising in case of bad response

data = response.json()
iss_position = (float(data["iss_position"]["latitude"]), float(data["iss_position"]["longitude"]))

parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0,
    "tzid": "Asia/Kolkata"
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json().get("results")
sunrise = data.get("sunrise").split("T")[1].split("+")[0]
sunset = data.get("sunset").split("T")[1].split("+")[0]
now = dt.datetime.now()


def check_night(sunrise_time, sunset_time, now_time):
    sunrise_dt = dt.datetime.strptime(sunrise_time, "%H:%M:%S")
    sunset_dt = dt.datetime.strptime(sunset_time, "%H:%M:%S")
    return not (sunrise_dt.time() < now_time.time() < sunset_dt.time())


def check_overhead(lat, long, cur_lat, cur_long, offset):
    return lat - offset < cur_lat < lat + offset and long - offset < cur_long < long + offset


def send_email(username, password):
    message = "Subject:ISS Tracker\n\nLOOK UP!"
    if (check_overhead(LAT, LONG, iss_position[0], iss_position[1], ALLOWED_DIFFERENCE)
            and check_night(sunrise, sunset, now)):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(username, password)
            connection.sendmail(from_addr=username, to_addrs=username, msg=message)
        print("EMAIL SENT")


while True:
    send_email(USERNAME, PASSWORD)
    time.sleep(TIMER)
