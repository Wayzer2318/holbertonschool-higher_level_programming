#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    devisible = []
    for item in my_list:
        if item % 2 == 0:
            devisible.append(True)
        else:
            devisible.append(False)
    return devisible
