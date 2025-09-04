#!/usr/bin/env python3

# Title:        solution2.py
# Description:  part2
# Author:       Chris Taylor m276342
# Creds:
# - https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

word_dict = {}

with open("./words.txt", "r") as f:

    for line in f:
        words = line.split(" ")

        for word in words:

            word = word.strip().lower()
            if word == "":
                continue

            elif word in word_dict:
                word_dict[word] = word_dict[word] + 1

            else:
                word_dict[word] = 1

word_dict = sorted(word_dict.items(), key=lambda item: item[1], reverse=True)
for i in range(5):
    print(f"{word_dict[i][0]}: {word_dict[i][1]}")
