from datetime import datetime,timedelta

date1 = datetime.now()

date2 = date1 - timedelta(days = 5)

result = (date1 - date2).total_seconds()

print("Difference between 2 dates in seconds: ", result, "seconds")