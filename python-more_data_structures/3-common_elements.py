#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_1 = set(set_1)
    set_2 = set(set_2)

    if(set_1 & set_2):
        return (set_1 & set_2)
    return []
