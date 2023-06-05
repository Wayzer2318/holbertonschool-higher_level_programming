#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        copy = my_list
        return copy
    elif idx not in range(len(my_list)):
        copy = my_list
        return copy
    my_list[idx] = element
    return my_list
