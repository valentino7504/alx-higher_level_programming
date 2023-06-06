#!/usr/bin/python3
import random
number = random.randint(-10, 10)
printed_string = "is zero"
if number > 0:
    printed_string = "is positive"
elif number < 0:
    printed_string = "is negative"
print(f"{number:d}", printed_string)
