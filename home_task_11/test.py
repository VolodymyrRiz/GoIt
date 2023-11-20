from collections import UserDict
from datetime import date, datetime
import os
import re


day_now = date.today()
print(day_now)

s = date(2023, 12, 12)
print(s)
d = s - day_now
print(d)