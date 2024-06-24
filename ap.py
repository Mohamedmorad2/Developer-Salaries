from datetime import datetime
now = datetime.now()
current_date = now.date()
current_time = now.strftime('%I:%M:%S %p')


print(f"Date {current_date}")
print(f"Time {current_time}")
