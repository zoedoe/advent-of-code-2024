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
    for number in range(len(update)):
        for previous_number in update[:number]:
            for rule in [x for x in rules if x[0] == update[number]
                         and x[1] == previous_number]:
                return 0
    return update[int(len(update) / 2)]


correct_updates = 0
for update in updates:
    check = check_rules(update)
    correct_updates += check

print(f"Valid update sum: {correct_updates}")
