#!/usr/bin/python3
"""returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """make  change"""
    # Initialize a variable to store the perimeter.

    perimeter = 0

    # Loop through each cell in the grid.
    for i, row in enumerate(grid):
        for j, element in enumerate(row):

            # For each land cell,add 4 to the perimeter and
            # then check the adjacent cells to subtract for shared edges.
            # print(element)
            if element == 1:
                perimeter += 4
                # print(f"Land found at ({i},{j}), adding 4 to perimeter")
                # Check the cell above (i-1, j):
                if i > 0 and grid[i-1][j] == 1:
                    # If it's land, subtract 1 from the perimeter.
                    perimeter -= 1
                # Check the cell below (i+1, j):
                if i < len(grid) - 1 and grid[i+1][j] == 1:
                    # If it's land, subtract 1 from the perimeter.
                    perimeter -= 1
                # Check the cell to the left (i, j-1):
                if j > 0 and grid[i][j-1] == 1:
                    # If it's land, subtract 1 from the perimeter.
                    perimeter -= 1
                # Check the cell to the right (i, j+1):
                if j < len(row) - 1 and grid[i][j+1] == 1:
                    # If it's land, subtract 1 from the perimeter.
                    perimeter -= 1
    # Return the total perimeter at the end.
    return perimeter
