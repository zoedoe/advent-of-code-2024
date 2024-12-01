# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 10:43:07 2024

@author: zoë
"""

import numpy as np


list_one = []
list_two = []

with open("input", "r") as file:
    data = file.readlines()
    file.close()

for row in data:
    washed = row.strip("\n").split(" ")
    list_one.append(int(washed[0]))
    list_two.append(int(washed[-1]))

list_one.sort()
list_two.sort()

similarity = 0
for number in list_one:
    indices = [i for i, item in enumerate(list_two) if item == number]
    similarity += number * len(indices)

list_one = np.array(list_one)
list_two = np.array(list_two)

list_difference = np.abs(list_one - list_two)
print(f"Total distance is: {np.sum(list_difference)}")
print(f"Similarity score is: {similarity}")
