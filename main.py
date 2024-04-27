import random
import pandas
import smtplib
import datetime

EMAIL_ADDRESS = '<EMAIL>'
PASSWORD = '<PASSWORD>'
now = datetime.datetime.now()
day = now.day
month = now.month

df = pandas.read_csv('birthdays.csv')
data = df.to_dict(orient='records')
receiver_email = data['email']

for _ in range(0, len(data)):
    if data[_]["month"] == month and data[_]["day"] == day:
        with open(f"./letter_templates/letter_{random.randint(1, 3)}") as template:
            letter_template = template.read()
            letter = letter_template.replace("[NAME]", data[_]["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL_ADDRESS, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL_ADDRESS, to_addrs=receiver_email,
                                msg=f"Subject: Happy Birthday\n\n{letter}")


# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



