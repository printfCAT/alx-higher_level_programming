#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    x1, y1 = a[:2]
    x2, y2 = b[:2]
    x = x1 + x2
    y = y1 + y2
    return (x, y)
