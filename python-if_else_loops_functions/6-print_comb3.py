#!/usr/bin/python3
for i in range(0, 10):
    for y in range(0, 10):
        if i < y:
            if i == 8 and y == 9:
                print("{:d}{:d}".format(i, y))
            else:
                print("{:d}{:d}, ".format(i, y), end='')
