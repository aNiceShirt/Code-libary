##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random
import pandas
import datetime as dt
import smtplib

my_email = "mathias.bhelnaes@gmail.com"
password = ""

data = pandas.read_csv("day-32_email/Birthday_wisher/birthdays.csv")

today = dt.datetime.now()
today_month, today_day = today.month, today.day

print(len(data))

for i in range(0, len(data)):
    if today_month == data['month'][i] and today_day == data['day'][i]:
        letter_num = random.randint(1, 3)
        with open("day-32_email/Birthday_wisher/letter_templates/letter_" + str (letter_num) + ".txt") as letter:
            letter_lines = letter.readlines()
            letter_lines[0] = letter_lines[0].replace("[NAME]", data['name'][i])
            letter = ""
            for sentence in letter_lines:
                letter += sentence
            print(letter)
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=data['email'][i], 
                                    msg="Subject:Happy birthday \n\n "+ letter)


