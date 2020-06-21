"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from itertools import *
from collections import *
from datetime import *

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the timeline? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
d = defaultdict(int)


for i, r, t, l in calls:
    date = datetime.strptime(t, "%d-%m-%Y %H:%M:%S")
    if date.year == 2016 and date.month == 9:
        d[i] += int(l)
        d[r] += int(l)

print(
    f"{max(d.items(), key=lambda i: i[1])[0]} spent the longest time, {max(d.items(), key=lambda i: i[1])[1]} seconds, on the phone during September 2016.")
