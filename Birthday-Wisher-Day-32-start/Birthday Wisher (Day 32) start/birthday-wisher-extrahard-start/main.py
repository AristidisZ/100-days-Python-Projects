##################### Extra Hard Starting Project ######################

import datetime as dt
import pandas as pd
import random
import smtplib

now = dt.datetime.now()
day = now.day
month = now.month
# print(month, day)

my_email = "haricatest@gmail.com"
password = "wyty qkaa xcym fvkt"


data = pd.read_csv("birthdays.csv")

today_birthday = data[(data["month"] == month) & (data["day"] == day)]
print(today_birthday)


# for index, row in today_birthday.iterrows():
#     name = row["name"]
#     email = row["email"]
#     random_letter = random.randint(1, 3)
#     with open(f"./letter_templates/letter_{random_letter}.txt", "r") as letter:
#         letter_content = letter.read()
#         updated_letter_content = letter_content.replace("[NAME]", name)
#
#     with smtplib.SMTP("smtp.gmail.com", 587) as connect:
#         connect.starttls()  # make connection secure
#         connect.login(user=my_email, password=password)
#         print("login success")
#         connect.sendmail(from_addr=my_email,
#                          to_addrs="aristidiszotka@gmail.com",
#                          msg=f"Subject:Happy Birthday\n\n{updated_letter_content}")
#         print("email send")

