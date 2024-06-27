import smtplib

import datetime as dt
import pandas as pd
import random

with open("./quotes.txt", "r") as data:
    data = data.readlines()

random_quote = random.choice(data)

my_email = "haricatest@gmail.com"
password = "wyty qkaa xcym fvkt"

now = dt.datetime.now()
year = now.year
mont = now.month
day_of_week = now.weekday()

data_of_birth = dt.datetime(1997, 3, 17)
print(day_of_week)
#
# if day_of_week == 4:
#     with smtplib.SMTP("smtp.gmail.com", 587) as connect:
#         connect.starttls()  # make connection secure
#         connect.login(user=my_email, password=password)
#         print("login success")
#         connect.sendmail(from_addr=my_email,
#                          to_addrs="aristidiszotka@gmail.com",
#                          msg=f"Subject:Motivation\n\n{random_quote}")
#         print("email send")

