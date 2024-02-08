#!/usr/bin/python3
"""
N queens problem
"""
import sys


def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, row, n, solutions):
    if row == n:
        # Add the current solution to the list
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            solve_nqueens_util(board, row + 1, n, solutions)

            board[row][col] = 0


def solve_nqueens(n):
    # Initialize the chessboard
    board = [[0] * n for _ in range(n)]
    solutions = []

    solve_nqueens_util(board, 0, n, solutions)

    return solutions


size = int(sys.argv[1])
if isinstance(size, int) is False:
    print("N must be a number")
    sys.exit(1)
if size < 4:
    print("N must be at least 4")
    sys.exit(1)
solutions = solve_nqueens(size)
for solution in solutions:
    print(solution)
