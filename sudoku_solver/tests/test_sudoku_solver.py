import pytest
from unittest import mock
import sys
sys.path.append('..\Sudoku_solver')
from scripts.sudoku_solver import SudokuSolver

def test_sudoku_solver_with_hard_sudoku():
        test_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [3, 0, 0, 0, 7, 0, 0, 8, 0],
                    [0, 8, 1, 6, 0, 0, 0, 0, 0],
                    [8, 0, 0, 2, 5, 0, 0, 6, 0],
                    [0, 6, 4, 0, 0, 1, 0, 0, 7],
                    [5, 0, 0, 0, 0, 6, 8, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 3, 0],
                    [7, 2, 0, 0, 0, 3, 0, 0, 4],
                    [0, 0, 0, 4, 0, 5, 1, 0, 2]]
        test_sudoku_solve = SudokuSolver(test_board)
        test_sudoku_solve.solve()
        expected_sudoku_result = [[4, 5, 7, 1, 2, 8, 3, 9, 6],
                                  [3, 9, 6, 5, 7, 4, 2, 8, 1],
                                  [2, 8, 1, 6, 3, 9, 7, 4, 5],
                                  [8, 1, 3, 2, 5, 7, 4, 6, 9],
                                  [9, 6, 4, 3, 8, 1, 5, 2, 7],
                                  [5, 7, 2, 9, 4, 6, 8, 1, 3],
                                  [1, 4, 5, 7, 6, 2, 9, 3, 8],
                                  [7, 2, 9, 8, 1, 3, 6, 5, 4],
                                  [6, 3, 8, 4, 9, 5, 1, 7, 2]]
        assert test_sudoku_solve.board == expected_sudoku_result

def test_sudoku_solver_with_invalid_sudoku():
        test_board = [[3, 0, 0, 0, 0, 0, 0, 0, 0],
                    [3, 0, 0, 0, 7, 0, 0, 8, 0],
                    [0, 8, 1, 6, 0, 0, 0, 0, 0],
                    [8, 0, 0, 2, 5, 0, 0, 6, 0],
                    [0, 6, 4, 0, 0, 1, 0, 0, 7],
                    [5, 0, 0, 0, 0, 6, 8, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 3, 0],
                    [7, 2, 0, 0, 0, 3, 0, 0, 4],
                    [0, 0, 0, 4, 0, 5, 1, 0, 2]]
        test_sudoku_solve = SudokuSolver(test_board)
        test_sudoku_solve.solve()
        assert test_sudoku_solve.solve() == False
