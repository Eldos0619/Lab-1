from datetime import datetime

current_date = datetime.now()

date_without_microseconds = current_date.replace(microsecond=0)

print("Date without microseconds: ", date_without_microseconds)