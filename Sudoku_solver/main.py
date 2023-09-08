from scripts.sudoku_reader import SudokuReader
from scripts.sudoku_solver import SudokuSolver

sudoku = SudokuReader('sudoku.txt')
sudoku_solved = SudokuSolver(sudoku.prepare_sudoku_to_solve())
print(sudoku.prepare_sudoku_to_solve())