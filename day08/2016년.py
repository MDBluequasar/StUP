a = 5
b = 24         # a월 b일
day = ['FRI','SAT','SUN','MON','TUE','WED','THU',]

# 1월 1일은 금요일

import datetime

start = datetime.date(2016,1,1)
end = datetime.date(2016,a,b)
values = end - start
DDay = values.days

an = DDay % 7
result = day[an]

print(result)