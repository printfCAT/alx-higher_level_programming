#!/usr/bin/python3
def no_c(my_string):
    i = 0
    new_string = ''
    while i < len(my_string):
        if my_string[i] != 'C' and my_string[i] != 'c':
            new_string += my_string[i]
        i += 1
    return new_string
