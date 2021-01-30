#importy bibliotek
#math
import math
from math import sqrt

# print(math.sqrt(2))
# print(sqrt(2))


#random
#generowanie losowych intów, floatów, random choice
import random
random_integer = random.randint(0, 10)
# print(random_integer)
random_float = random.random()
# print(random_float)

list_of_integers = [1, 2, 3, 4, 5]
random_int_from_list = random.choice(list_of_integers)
# print(random_int_from_list)

#datetime
import datetime

now = datetime.datetime.now()
# print(now)
# print(now.date())
# print(now.time())
# print(now.isoformat())
# #strptime
# #strftime
# print(now.strftime("%d.%m.%Y %H:%M:%S"))
postrptime = datetime.datetime.strptime("18.01.2021 21:26:03", "%d.%m.%Y %H:%M:%S")
# print(postrptime.time())

ta_sama_pora_wczoraj = now - datetime.timedelta(days=1)
print(now, ta_sama_pora_wczoraj)

if now > ta_sama_pora_wczoraj:
    print("OK")
else:
    print("Nie ok")

#formaty - iso i inne
#timedelta


