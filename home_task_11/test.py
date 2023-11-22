from collections import UserDict
from datetime import date, datetime, timedelta
import os
import re


day_now = date.today()
print(day_now)

s = date(2000, 12, 23)
# x = re.findall("[0-9][0-9][0-9][0-9][-][0-9][0-9][-][0-9][0-9]", str(s))
# if x:
#     print('hhhhhhhhhhhhhhhhhhhhh')
# else:
#     print('NO')
print(s)
d = (s - day_now).days
d = int(d)

print(d)

delta = timedelta(days = d).days
print(delta)
try:
    birth = date('', '', '')
    print(birth)
except:
    pass
d = input()
print(chr(d))




