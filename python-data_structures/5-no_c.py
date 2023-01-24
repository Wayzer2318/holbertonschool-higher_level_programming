#!/usr/bin/python3
def no_c(my_string):
    nstring = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            nstring = nstring + i
    return nstring
