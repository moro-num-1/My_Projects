import datetime

date = datetime.date(2025, 5, 2)
today = datetime.date.today()
time = datetime.time(1, 59, 38)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %m-%d-%Y")

target_date_time = datetime.datetime(2024, 2, 7)
current_date_time = datetime.datetime.now()

if current_date_time > target_date_time:
    print("Target time has passed")
else:
    print("Target time has NOT passed")