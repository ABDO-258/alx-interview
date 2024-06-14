#!/usr/bin/python3
"""scribt to  rotate a matrix 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """rotate a matrix 90 degrees"""
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix[j][i])
        new_row.reverse()
        matrix.append(new_row)
    del matrix[:rows]
