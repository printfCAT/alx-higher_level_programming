#!/usr/bin/python3
def max_integer(my_list=[]):
    i = 0
    if not my_list:
        return None
    else:
        largest_int = my_list[0]
        while i < len(my_list):
            if my_list[i] > largest_int:
                largest_int = my_list[i]
            i += 1
        return largest_int
