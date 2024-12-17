"""
--- Day 1: Trebuchet?! ---
"""

import re

input = open("day1input.txt", "r")
content = input.read()
calValues = content.split()
input.close()

spelled_digits = {
    "zero": 0, 
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6, 
    "seven": 7, 
    "eight": 8, 
    "nine": 9
    }

total = 0
for v in calValues:
    first = -1
    firstindex = -1
    last = -1
    lastindex = -1
    # identify first and last numeric digits
    for index in range(len(v)): 
        digit = v[index]
        if digit.isnumeric(): 
            if first < 0: 
                first = int(digit)
                firstindex = index
            last = int(digit)
            lastindex = index
    
    # identify spelled digits 
    for d in spelled_digits.keys(): 
        indices = [m.start() for m in re.finditer(d, v)]
        if len(indices) > 0: 
            if indices[0] < firstindex: 
                firstindex = indices[0]
                first = spelled_digits[d]
            if indices[-1] > lastindex:
                lastindex = indices[-1]
                last = spelled_digits[d]
    total += 10*first + last

print(total)