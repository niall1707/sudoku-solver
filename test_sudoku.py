import unittest
from sudoku import sudoku_solver

def print_board(board):
    """Helper function to print the Sudoku board in a readable format."""
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

class TestSudokuSolver(unittest.TestCase):

    def test_valid_solution(self):
        print("\nRunning test_valid_solution...")
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        print("Input Board:")
        print_board(board)
        solution = sudoku_solver(board)
        print("\nSolved Board:")
        print_board(solution)
        self.assertIsNotNone(solution)

    def test_invalid_input(self):
        print("\nRunning test_invalid_input...")
        invalid_board = [[5, 3, 0, 0]]  # Not a valid 9x9 board
        print("Invalid Input Board:")
        print(invalid_board)
        with self.assertRaises(ValueError):
            sudoku_solver(invalid_board)

    def test_unsolvable_board(self):
        print("\nRunning test_unsolvable_board...")
        unsolvable_board = [
            [5, 5, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        print("Unsolvable Input Board:")
        print_board(unsolvable_board)
        result = sudoku_solver(unsolvable_board)
        print("\nResult (should be None):", result)
        self.assertIsNone(result)

    def test_empty_board(self):
        print("\nRunning test_empty_board...")
        empty_board = [[0] * 9 for _ in range(9)]
        print("Empty Input Board:")
        print_board(empty_board)
        solution = sudoku_solver(empty_board)
        print("\nSolved Board:")
        print_board(solution)
        self.assertIsNotNone(solution)

if __name__ == "__main__":
    unittest.main()
