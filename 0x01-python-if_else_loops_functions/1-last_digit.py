#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last = int(repr(number)[-1])

if last > 5 and number > 0:
    print("Last digit of", number, "is", last, "and is greater than 5")
elif last == 0:
    print("Last digit of", number, "is", last, "and is 0")
else:
    if number < 0:
        print("Last digit of {} is -{} and is less than 6 and not 0".format(number, last))
    else:
        print("Last digit of", number, "is", last, "and is less than 6 and not 0")
