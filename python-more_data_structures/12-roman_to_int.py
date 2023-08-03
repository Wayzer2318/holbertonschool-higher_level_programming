#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    if roman_string is None:
        return 0
    if type(roman_string) is not str:
        return 0
    roman_int = 0
    for i in range(len(roman_string) - 1):
        if roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
            roman_int += roman_dict[roman_string[i]] \
                    - 2 * roman_dict[roman_string[i]]
        else:
            roman_int += roman_dict[roman_string[i]]
    roman_int += roman_dict[roman_string[-1]]
    return roman_int
