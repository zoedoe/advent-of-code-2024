# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:08:01 2024

@author: zoë
"""

import numpy as np


def run_checks(difference_list):
    increasing_flag = 0
    fail_pos = -1
    for pos in range(len(difference_list)):
        if difference_list[0] >= 0:
            increasing_flag = 1
        if not abs(difference_list[pos]) >= 1:
            fail_pos = pos
            break
        elif not abs(difference_list[pos]) <= 3:
            fail_pos = pos
            break
        elif increasing_flag == 1:
            if not difference_list[pos] >= 0:
                fail_pos = pos
                break
        else:
            if not difference_list[pos] < 0:
                fail_pos = pos
                break
    return fail_pos


with open("input", "r") as file:
    data = file.readlines()
    file.close()

safe_reports = 0
for report in data:
    report = report.strip("\n").split(" ")
    difference_list = []
    sign_list = []
    for level in range(len(report) - 1):
        difference_list.append(int(report[level + 1]) - int(report[level]))
    fail_pos = run_checks(difference_list)
    if fail_pos == -1:
        safe_reports += 1
    else:
        for attempt in range(len(report)):
            mod_report = report.copy()
            del mod_report[attempt]
            difference_list = []
            for level in range(len(mod_report) - 1):
                difference_list.append(int(mod_report[level + 1])
                                       - int(mod_report[level]))
            try_success = run_checks(difference_list)
            if try_success == -1:
                safe_reports += 1
                break

print(f"Number of safe and dampened reports: {safe_reports}")
