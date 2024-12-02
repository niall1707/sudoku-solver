def sudoku_solver(board):
    """
    Solves a given sudoku board using backtracking.
    Input: board - a 9x9 grid represented as a list of lists
    Output: Solved board as a list of lists, or None if unsolvable
    """
    def is_valid(num, row, col):
        # Check the row
        if num in board[row]:
            return False

        # Check the column
        if num in [board[i][col] for i in range(9)]:
            return False

        # Check the subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def solve():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:  # Find an empty spot
                    for num in range(1, 10):
                        if is_valid(num, row, col):
                            board[row][col] = num
                            if solve():
                                return True
                            board[row][col] = 0  # Backtrack
                    return False
        return True

    if not solve():
        return None
    return board
