#!/usr/bin/python3
import random

number = random.randint(-10, 10)

# Do not touch the above lines

if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
