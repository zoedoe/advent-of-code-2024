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
        if puzzle[row, column] == "X":
            adjacent_cells = adjacent(column, row, puzzle)
            seq_m = check_letter(adjacent_cells, column, row, "M")
            for m in seq_m:
                check_x = direction(column, m[0])
                check_y = direction(row, m[1])
                try:
                    if (m[1] + 2*check_y >= len(puzzle)) or (m[0] + 2*check_x >= len(puzzle[0])) or (m[1] + 2*check_y < 0) or (m[0] + 2*check_x < 0):
                        continue
                    elif puzzle[m[1] + check_y, m[0] + check_x] == "A":
                        if puzzle[m[1] + 2*check_y, m[0] + 2*check_x] == "S":
                            xmas += 1
                except IndexError:
                    continue

print(f"Number of XMASes: {xmas}")
