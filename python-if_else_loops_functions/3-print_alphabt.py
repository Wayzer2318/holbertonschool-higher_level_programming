#!/usr/bin/python3
for i in range(97, 123):
    if i == 102 or i == 114:
        continue
    print(chr(i) + 0 * "{:02}".format(0), end="")
