# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:08:01 2024

@author: zoë
"""

import numpy as np


with open("input", "r") as file:
    data = file.readlines()
    file.close()

safe_reports = 0
for report in data:
    print(safe_reports)
    report = report.strip("\n").split(" ")
    print(report)
    difference_list = []
    sign_list = []
    for level in range(len(report) - 1):
        difference_list.append(int(report[level + 1]) - int(report[level]))
    print(difference_list)
    difference_list = np.array(difference_list)
    if (np.abs(difference_list) >= 1).all():
        if (np.abs(difference_list) <= 3).all():
            if difference_list[0] > 0:
                if (difference_list > 0).all():
                    safe_reports += 1
            elif difference_list[0] < 0:
                if (difference_list < 0).all():
                    safe_reports += 1

print(f"Number of safe reports: {safe_reports}")
