from datetime import datetime, timedelta

today = datetime.now()

yesterday = today - timedelta(days=1)

tomorrow = today + timedelta(days=1)

print("Today: ", today.strftime("%d-%m-%Y"))
print("Yesterday: ", yesterday.strftime("%d-%m-%Y"))
print("Tomorrow: ", tomorrow.strftime("%d-%m-%Y"))