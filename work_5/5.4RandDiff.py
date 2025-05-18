import random
from datetime import datetime, timedelta

dates = []
today = datetime.now()
for _ in range(10):
    random_days = random.randint(0, 5*365)  
    date = today - timedelta(days=random_days)
    dates.append(date)

for i in range(1, 10):
    diff = (dates[i] - dates[i-1]).days
    print(f"Разница между {dates[i-1].date()} и {dates[i].date()}: {abs(diff)} дней")