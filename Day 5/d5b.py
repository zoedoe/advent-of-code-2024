# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:21:38 2024

@author: zoë
"""

with open("input", "r") as file:
    data = file.readlines()

rules = [list(map(int, row.strip("\n").split("|")))
         for row in data if row.count("|") == 1]
updates = [list(map(int, row.strip("\n").split(",")))
           for row in data if row.count(",") >= 1]


def check_rules(update):
    global rules
    for number in range(len(update)):  # for each number in the update
        for previous_number in update[:number]:  # get every number before hand
            for rule in [x for x in rules if x[0] == update[number]  # find only broken rules
                         and x[1] == previous_number]:
                return 0  # return 0 if any rule is broken
    return update[int(len(update) / 2)]  # return midpoint


def fix_update(update):
    global rules
    while check_rules(update) == 0:  # run while update breaks any rules
        for number in range(len(update)):
            for previous_number in range(len(update[:number])):
                for rule in [x for x in rules if x[0] == update[number]
                             and x[1] == update[previous_number]]:  # bubble sort at each rule break
                    update[number], update[previous_number] = update[previous_number], update[number]
    return update


correct_updates = 0
incorrect_fixed = 0
for update in updates:
    check = check_rules(update)
    correct_updates += check
    if check == 0:
        update = fix_update(update)
        incorrect_fixed += check_rules(update)

print(f"Valid update sum: {incorrect_fixed}")
