#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """
     function that returns a list of lists of integers
     representing the Pascal’s triangle of n:
    """
    list1 = []
    if n <= 0:
        return list1
    for row in range(n):
        row_elements = [1] * (row + 1)
        for col in range(1, row):
            row_elements[col] = list1[row - 1][col - 1] + list1[row - 1][col]
        list1.append(row_elements)
    return list1
