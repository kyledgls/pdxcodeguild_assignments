"""
sock sorter
original version by Kyle Douglas
"""
import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']
i = 0
laundry = []
while i < 100:
    laundry.append(random.choice(sock_types))
    i += 1
print(laundry)






