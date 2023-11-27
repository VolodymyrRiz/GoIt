import json
from datetime import date, datetime, timedelta



some_data = {'key': 'a', 2: [1, 2, 3], 'tuple': (10, 16), 'a': {'key': 'value'}}

file_name = 'data.json'

with open(file_name, "w") as fh:
   json.dump(some_data, fh)


with open(file_name, "r") as fh:
    unpacked = json.load(fh)
    print(unpacked)


# unpacked is some_data    # False
# unpacked == some_data    # False
# print(some_data)

# unpacked['key'] == some_data['key']     # True
# unpacked['a'] == some_data['a']         # True
# unpacked['2'] == some_data[2]           # True
# unpacked['tuple'] == [5, 6]             # True