# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:37:50 2024

@author: zoë
"""

import re


with open("input", "r") as file:
    data = file.readlines()


regex = re.compile(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)")

enabled = 1
product_sum = 0
for row in data:
    valid_sequences = re.findall(regex, row)
    for item in valid_sequences:
        if item[2] == "(":
            enabled = 1
        elif item[2] == "n":
            enabled = 0
        else:
            nums = item.strip(")").strip("mul(").split(",")
            product = int(nums[0]) * int(nums[1]) * enabled
            product_sum += product

print(f"Sum of all products: {product_sum}")
