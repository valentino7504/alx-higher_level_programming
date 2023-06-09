#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ != "__main__":
    exit()
argv = sys.argv
if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
a = int(argv[1])
b = int(argv[3])
operation = argv[2]
if operation not in ["+", "-", "*", "/"]:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
c = int()
if operation == "+":
    c = add(a, b)
elif operation == "-":
    c = sub(a, b)
elif operation == "*":
    c = mul(a, b)
else:
    c = div(a, b)
print(f"{a} {operation} {b} = {c}")
