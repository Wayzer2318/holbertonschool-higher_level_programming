#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return
    mv = 0
    for i in range(1, my_list):
        if i > mv:
            mv = i
    return mv
