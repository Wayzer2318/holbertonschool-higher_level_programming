#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    tuple1 = tuple_a[0] + tuple_b[0]
    tuple2 = tuple_a[1] + tuple_b[1]
    return tuple1, tuple2
