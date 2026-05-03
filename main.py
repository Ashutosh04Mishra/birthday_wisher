import smtplib
import random
import datetime as dt
import pandas as pd
import os

now = dt.datetime.now()
today_month = now.month
today_day = now.day

today = (today_month, today_day)

df = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row['month'],data_row['day']): data_row for (index, data_row) in df.iterrows()}

if (today_month, today_day) in birthdays_dict :
    person = birthdays_dict[today]
    name = person["name"]

    choice = random.randint(1,3)
    with open(f"letter_templates/letter_{choice}.txt") as f:
        contents = f.read()

    birthday_msg = contents.replace("[NAME]", name)

    my_email = os.environ.get("MY_EMAIL")
    password = os.environ.get("MY_PASSWORD")

    receiver = birthdays_dict[today]
    receiver_mail = receiver["email"]

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection :
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver_mail,
            msg=f"Subject:HAPPY BIRTHDAY!!\n\n{birthday_msg}"
        )
