#!/usr/bin/python3
import sys

num_args = len(sys.argv) - 1

if num_args == 0:
    print("0 arguments.")
    sys.exit()
elif num_args == 1:
    print("1 argument:")
else:
    print(num_args, "arguments:")

for i in range(1, num_args + 1):
    print("{}: {}".format(i, sys.argv[i]))
