#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while True:
        try:
            while i != x:
                print("{}".format(my_list[i]), end="")
                i += 1
        except Exception as e:
            pass
        finally:
            print()
            return i
