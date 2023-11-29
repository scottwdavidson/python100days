import datetime as dt

# Now
now = dt.datetime.now()
print (now)

if now.year == 2023:
    print("It's 2023 ... ")

# My birthdate
birthdate = dt.datetime(year=1965, month=2, day=21, hour=9, minute=24)
print(f"my birthdate: {birthdate}")