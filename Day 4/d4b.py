# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:48:49 2024

@author: zoë
"""

import numpy as np

with open("input", "r") as file:
    data = file.readlines()


def adjacent(coord_x, coord_y, puzzle):
    adjacent_cells = []
    for i in [coord_y - 1, coord_y, coord_y + 1]:
        horiz_slice = []
        if (i < 0) or (i >= len(puzzle)):
            horiz_slice = [0, 0, 0]
        else:
            for j in [coord_x - 1, coord_x, coord_x + 1]:
                if (j < 0) or (j >= len(puzzle[0])):
                    cell = 0
                else:
                    cell = puzzle[i][j]
                horiz_slice.append(cell)
        adjacent_cells.append(horiz_slice)
    return adjacent_cells


def check_letter(section, coord_x, coord_y, target_letter):
    y = -1
    valid_locations = []
    for j in section:
        x = -1
        for i in j:
            if i == target_letter:
                valid_locations.append([coord_x + x, coord_y + y])
            x += 1
        y += 1
    return valid_locations


def direction(pos_one, pos_two):
    if pos_one < pos_two:
        return 1
    elif pos_one == pos_two:
        return 0
    elif pos_one > pos_two:
        return -1


puzzle = []
for row in data:
    row = row.strip("\n")
    horiz_slice = []
    for letter in row:
        horiz_slice.append(letter)
    puzzle.append(horiz_slice)
puzzle = np.array(puzzle)

xmas = 0
for row in range(len(puzzle)):
    for column in range(len(puzzle[0])):
        if puzzle[row, column] == "A":
            adjacent_cells = adjacent(column, row, puzzle)
            seq_m = check_letter(adjacent_cells, column, row, "M")
            seq_s = check_letter(adjacent_cells, column, row, "S")
            if len(seq_m) >= 2 and len(seq_s) >= 2:
                m_dirs = []
                s_dirs = []
                for m in seq_m:
                    m_dirs.append(direction(column, m[0])
                                  + direction(row, m[1]))
                for s in seq_s:
                    s_dirs.append(direction(column, s[0])
                                  + direction(row, s[1]))
                if (0 in m_dirs) and ((2 in m_dirs) or (-2 in m_dirs)):
                    if (0 in s_dirs) and ((2 in s_dirs) or (-2 in s_dirs)):
                        xmas += 1

print(f"Number of XMASes: {xmas}")
