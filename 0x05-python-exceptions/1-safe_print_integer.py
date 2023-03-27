#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            value = int(value)
            print("{:d}".format(value), end="\n")
            return True
    except TypeError:
        print("{} is not an integer".format(value))
    return False
