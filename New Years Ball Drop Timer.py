from datetime import datetime

New_Years_Day = datetime.strptime('1/1/24', '%m/%d/%y').date()
today_date = datetime.now().date()

years = today_date.year - New_Years_Day.year
months = today_date.month - New_Years_Day.month
days = today_date.day - New_Years_Day.day

years = New_Years_Day.year -today_date.year
months = New_Years_Day.month -today_date.month
days = New_Years_Day.day -today_date.day
if months < 0:
    years -= 1
    months += 12

if days < 0:
    months -= 1
    days += 30

print(f"The Ball drops to ring in the new year in {months} months and {days} days.")