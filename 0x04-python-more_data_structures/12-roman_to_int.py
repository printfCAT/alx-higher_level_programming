#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    prev_value = 0
    
    for char in roman_string[::-1]:
        current_value = roman_dict[char]
        if current_value < prev_value:
            integer -= current_value
        else:
            integer += current_value
        prev_value = current_value
        
    return integer
