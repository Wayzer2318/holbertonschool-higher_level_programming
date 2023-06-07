#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = []
    for item in set_1:
        if item not in set_2:
            result.append(item)
    for item2 in set_2:
        if item2 not in set_1:
            result.append(item2)
    return result
