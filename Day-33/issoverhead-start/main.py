import requests
from datetime import datetime
import smtplib

MY_LAT = 40.667242  # Your latitude
MY_LONG = 22.891723  # Your longitude


def iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_longitude, iss_latitude)

    if MY_LAT - 10 <= iss_latitude <= MY_LAT + 10 and MY_LONG - 10 <= iss_longitude <= MY_LONG + 10:
        return True


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

    print("Sunrise", sunrise, "Sunset", sunset)
    print(time_now.hour)

    if time_now.hour >= sunset:
        return True


if iss_close() and is_night():
    my_email = "haricatest@gmail.com"
    password = "wyty qkaa xcym fvkt"

    with smtplib.SMTP("smtp.gmail.com", 587) as connect:
        connect.starttls()  # make connection secure
        connect.login(user=my_email, password=password)
        print("login success")
        connect.sendmail(from_addr=my_email,
                         to_addrs="aristidiszotka@gmail.com",
                         msg=f"Subject:Iss is above\n\n Look Up")
        print("email send")

else:
    print("Nothing Yet")

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
