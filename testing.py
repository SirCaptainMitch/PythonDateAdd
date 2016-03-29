
from dateadd import dateadd
from datetime import datetime, timedelta

today = datetime.today()
today_str = '2/27/2014'

# print(dateadd('m',2, today_str))
# print(dateadd('month',-2, today_str))
# print(dateadd('Month',-2, today_str))
# print(dateadd('MONTH',-2, today_str))

# print(dateadd('d',2, today_str))
# print(dateadd('day',-2, today_str))
# print(dateadd('Day',-2, today_str))
# print(dateadd('DAY',-2, today_str))

print(dateadd('y',2,today_str))
print(dateadd('year',-2,today_str))
print(dateadd('Year',200,today_str))
print(dateadd('YEAR',-200,today_str))
