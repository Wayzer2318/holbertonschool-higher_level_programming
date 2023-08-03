#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        copy1 = my_list.copy()
        return copy1
    elif idx not in range(len(my_list)):
        copy2 = my_list.copy()
        return copy2
    copy3 = my_list.copy()
    copy3[idx] = element
    return copy3
