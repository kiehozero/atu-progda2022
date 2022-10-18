import datetime

print("Check if it's Tuesday")

today = datetime.datetime.today()
dayofweek = today.weekday()

if dayofweek == 1:
    print("It's Tuesday or Wednesday")
elif dayofweek == 2:
    print("It's Wednesday")
else:
    print("It's not Tuesday or Wednesday")