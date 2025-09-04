#!/usr/bin/env python3

# Title:        solution1.py
# Description:  part1
# Author:       Chris Taylor m276342

with open("./numbers.txt", "r") as f:
    lines = sorted(f, key=float)
    for i in range(len(lines)):
        print(float(lines[i].strip()))
