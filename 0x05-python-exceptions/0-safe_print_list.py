#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for element in my_list[:x]:
            print("{}".format(element), end="")
            i += 1
        print()
    except IndexError:
        print("x larger than length of the list")
    return i
