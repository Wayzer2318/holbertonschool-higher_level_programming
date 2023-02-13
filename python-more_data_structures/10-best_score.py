#!/usr/bin/python3


def best_score(a_dictionary):
    result = 0
    for value in a_dictionary:
        if value > result:
            result = value
    return result
