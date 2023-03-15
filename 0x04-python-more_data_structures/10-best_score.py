#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    best_key = list(a_dictionary.keys())[0]
    best_value = a_dictionary[best_key]
    for key, value in a_dictionary.items():
        if value > best_value:
            best_key = key
            best_value = value
    return best_key
