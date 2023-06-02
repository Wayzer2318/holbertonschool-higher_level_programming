#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            a = ord(i)
            i = chr(a - 32)

        print("{}".format(i), end='')
    print()
