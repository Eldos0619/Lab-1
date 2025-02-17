from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=5)

new_date = new_date.strftime("%Y-%m-%d")

print(f"Result of subtracting five days from current date: {new_date}")