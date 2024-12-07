# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 05:04:28 2024

@author: zoë
"""

with open("input", "r") as file:
    data = file.readlines()


def try_operator(row):
    target = int(row.split(":")[0])
    nums = [int(x) for x in row.split(":")[1].strip("\n").split()]
    outcomes = []
    for number in range(len(nums) - 1):
        if len(outcomes) != 0:
            outcomes.extend(outcomes)
            for element in range(len(outcomes)):
                if element < int(len(outcomes) / 2):
                    outcomes[element] *= nums[number + 1]
                else:
                    outcomes[element] += nums[number + 1]
        else:
            outcomes.append(nums[number] * nums[number + 1])
            outcomes.append(nums[number] + nums[number + 1])
    if target in outcomes:
        return target
    else:
        return 0


calibration = 0
for row in data:
    calibration += try_operator(row)

print(f"Total calibration result: {calibration}")
