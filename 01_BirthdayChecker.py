from calendar import month
import datetime as dt

today = dt.date.today()
print(today, f"Today is {today:%A}")

print("\n"+5*"="+"Check Your Birthday"+"="*5+"\n")
year = int(input("Year \t\t: "))
month = int(input("Month \t\t: "))
dateInput = int(input("Date \t\t: "))
savedRes = dt.date(year,month,dateInput)
print(f"Your Birthdate \t\t: {savedRes}")
print(f"And you're birth on \t: {savedRes:%A} ")
age = today-savedRes
age_year = age.days // 365
print(f"Your age is \t\t: {age.days} days, or {age_year} years")
