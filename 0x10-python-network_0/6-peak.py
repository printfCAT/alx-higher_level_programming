#!/usr/bin/python3
def find_peak(list_of_integers):
    peaks = []
    if len(list_of_integers) < 1:
        return None
    elif len(set(list_of_integers)) == 1:
        return str(list_of_integers[0])
    elif len(list_of_integers) == 1:
        peaks.append(str(list_of_integers[0]))
    else:
        for i in range(len(list_of_integers) - 1):
            if i == 0:
                if list_of_integers[i] > list_of_integers[i + 1]:
                    peaks.append(str(list_of_integers[i]))
            elif i == len(list_of_integers) - 1:
                if list_of_integers[i] > list_of_integers[i - 1]:
                    peaks.append(str(list_of_integers[i]))
            else:
                if list_of_integers[i] > list_of_integers[i - 1] \
                   and list_of_integers[i] > list_of_integers[i + 1]:
                    peaks.append(str(list_of_integers[i]))
    return ", ".join(peaks)
