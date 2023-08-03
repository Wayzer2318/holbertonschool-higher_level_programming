#!/usr/bin/python3
def safe_print_integer(value):
    try:
        i = value - 1
        print("{:d}".format(value))
        return True
    except TypeError:
        return False
    except ValueError:
        return False
