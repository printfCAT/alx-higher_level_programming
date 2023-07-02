#!/usr/bin/python3
""" sorting list algorithm """


def find_peak(list_of_integers):
    """ returns a peak in a list of unsorted integers """
    if not list_of_integers:
        return None
    peak = list_of_integers[0]

    for num in list_of_integers:
        if num > peak:
            peak = num

    return peak
