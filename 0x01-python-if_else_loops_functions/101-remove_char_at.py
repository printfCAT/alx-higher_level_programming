#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    else:
        chars = list(str)
        del chars[n]
    return ''.join(chars)
