#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    set_1 = set(set_1)
    set_2 = set(set_2)
    
    for i in set_2:
        if i not in set_1:
            return i
    for i in set_1
        if i not in set_2:
            return i
