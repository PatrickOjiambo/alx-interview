#!/usr/bin/python3
"""
    island_perimeter - returns the perimeter
    of the island described in grid
"""
def island_perimeter(grid):
    """island_perimeter

    Args:
        grid (_type_): An array of arrays of integers

    Returns:
        int: The perimeter of the island
    """
    height = len(grid)
    width = len(grid[0])
    perimeter = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:  # Check the cell above
                    perimeter -= 2

                if j > 0 and grid[i][j - 1] == 1:  # Check the cell to the left
                    perimeter -= 2

    return perimeter
