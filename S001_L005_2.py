import datetime as dt

today_weekday = dt.date.today().strftime("%A")
print(today_weekday)

if today_weekday == 'Monday':
    print("I'm helping my mum")
elif today_weekday == 'Tuesday' or today_weekday == 'Wednesday':
    print("You are doing laundry")
elif today_weekday == 'Thursday':
    print("I'm on duty")
elif today_weekday == 'Friday':
    print("I have two meetings")
elif today_weekday == 'Saturday':
    print("You have lessons")
else:
    print("SUNDAY WILL BE FOR US")