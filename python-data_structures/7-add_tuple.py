#!/usr/bin/python3
def add_tupple(tuple_a=(), tuple_b=()):
    lista = list(tuple_a)
    listb = list(tuple_b)
    i = 0
    for i in range(len(lista)):
        i += 1
    if i > 2:
        lista[2:] = []
    if i == 1:
        lista += [0]
    if i == 0:
        lista += [0, 0]

    j = 0
    for j in range(0, len(listb)):
        j += 1
    if j > 2:
        listb[2:] = []
    if j == 1:
        listb += [0]
    if j == 0:
        listb += [0, 0]

    z = zip(lista, listb)
    sum = [x + y for (x, y) in z]
    sum = tuple(sum)
    return sum
