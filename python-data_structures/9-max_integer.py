#!/usr/bin/python3
def max_integer(my_list=[]):
    mv = 0
    for i in my_list:
        if i > mv:
            mv = i
    return mv
