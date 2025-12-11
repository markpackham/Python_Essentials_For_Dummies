import datetime as dt
# Get current date & time
now = dt.datetime.now()
# Make decision based on hour
if now.hour < 12:
    print("Good morning")
else:
    print("Good afternoon")
print("I hope you are doing well no matter the time")