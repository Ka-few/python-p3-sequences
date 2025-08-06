#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])  # No elements
    elif length == 1:
        print([0])  # Only the first number
    elif length == 2:
        print([0, 1])  # First two numbers
    else:
        fib = [0, 1]
        while len(fib) < length:
            fib.append(fib[-1] + fib[-2])
        print(fib)

print_fibonacci(20)
