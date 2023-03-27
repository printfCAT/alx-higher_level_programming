#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    quo_list = []
    for i in range(list_length):
        try:   
            quotient = my_list_1[i] / my_list_2[i]
            quo_list.append(quotient)
        except ZeroDivisionError:
            print("division by 0")
            quo_list.append(0)
        except TypeError:
            print("wrong type")
            quo_list.append(0)
        except IndexError:
            print("out of range")
            quo_list.append(0)
        finally:
            continue
    return quo_list
