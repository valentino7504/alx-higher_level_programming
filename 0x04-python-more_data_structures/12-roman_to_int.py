#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
    total = 0
    for i in range(len(roman_string)):
        current_letter = roman_string[i]
        if i < len(roman_string) - 1:
            next_letter = roman_string[i + 1]
        else:
            next_letter = None
        if not next_letter:
            total += roman_values[current_letter]
        elif roman_values[current_letter] < roman_values[next_letter]:
            total -= roman_values[current_letter]
        else:
            total += roman_values[current_letter]
    return total
