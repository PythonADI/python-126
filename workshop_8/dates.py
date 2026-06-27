# from datetime import date
import datetime as dt



# today = datetime.date(12, 12, 1)
today = dt.date(12, 12, 1)

print(today.year)
print(today.month)
print(today.day)
print(today.strftime("%d %B %Y"))
