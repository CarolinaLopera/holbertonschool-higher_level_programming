#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last = int(repr(number)[-1])
print(number, last)

if last > 5 and number > 0:
    print("Last digit of", number, "is", last, "and is greater than 5")
elif last == 0:
    print("Last digit of", number, "is", last, "and is 0")
elif (last < 6 and last != 0) or number < 0:
    if number < 0:
        print("Last digit of {} is ".format(number), end="")
        print("-{} and is less than 6 and not 0".format(last))
    else:
        print("Last digit of", number, "is ", end="")
        print(last, "and is less than 6 and not 0")
