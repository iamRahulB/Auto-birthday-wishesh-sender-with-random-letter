##################### Extra Hard CHALLENGE ######################
import datetime as dt
import random
import smtplib
import pandas

data=pandas.read_csv("./birthdays.csv")
day_list=data.days.to_list()
month_list=data.month.to_list()
name=data.name.to_list()

now=dt.datetime.now()
day_today=now.day
month_today=now.month

if day_today in day_list and month_today in month_list:
	with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter:
		chosen_letter=letter.read()
		sending_letter=chosen_letter.replace("[NAME]", name[day_list.index(day_today)])

	with smtplib.SMTP("smtp.gmail.com") as connect:
		connect.starttls()
		connect.login(user="yourmail@gmail.com",password="your pass")
		connect.sendmail(from_addr="yourmail@gmail.com",to_addrs="birthdayguymail@gmail.com",msg=f"Subject:Birthday wishes\n\n {sending_letter}")
	print(sending_letter)
