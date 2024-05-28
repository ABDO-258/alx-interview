#!/usr/bin/python3
"""scribt to check if data is a valid UTF-8"""

import sys


def print_solution(solution):
    """print the solution"""
    positions = []
    for row_index, row in enumerate(solution):
        for col_index, value in enumerate(row):
            if value == 1:
                positions.append([row_index, col_index])
    print(positions)


def nqueens(N):
    """the N queens problem"""
    # create the board
    board = []
    solutions = []
    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(0)
        board.append(row)
    placeQueens(board, 0, N, solutions)
    # print(solutions)
    for solution in sorted(solutions, reverse=True):
        print_solution(solution)


def safePlace(row, col, board):
    """"""
    # Check row and column conflicts
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal conflicts
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # Check lower diagonal conflicts
    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True


def placeQueens(board, col, N, solutions):
    """define where to place the queens recursively"""

    if col >= N:
        solutions.append([row[:] for row in board])
        return
    for i in range(N):
        if safePlace(i, col, board):
            board[i][col] = 1
            placeQueens(board, col + 1, N, solutions)
            board[i][col] = 0  # Backtrack


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    if N < 4:
        print('N must be at least 4')
    else:
        nqueens(N)
