#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_list = []
    i = 0
    try:
        for element in my_list[:x]:
            if isinstance(element, int):
                int_list.append(element)
                print("{:d}".format(element), end="")
                i += 1
        print()
    except IndexError:
        print("list index out of range")
    return i
