#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_list = []
    i = 0
    for element in my_list[:x]:
        if isinstance(element, int):
            element = int(element)
            int_list.append(element)
    try:
        for int_element in int_list:
            print("{:d}".format(int_element), end="")
            i += 1
        print()
    except (ValueError, TypeError):
        print("list index out of range")
    return i
