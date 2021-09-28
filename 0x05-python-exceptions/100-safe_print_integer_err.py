#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        # sys.stderr.write("Exception: ")
        # sys.stderr.write("Unknown format code 'd' for object of type 'str'")
        return False
