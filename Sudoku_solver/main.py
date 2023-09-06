from scripts.SudokuReader import SudokuReader
from scripts.SudokuSolver import SudokuSolver

sudoku = SudokuReader('sudoku.txt')

my_sudoku = SudokuSolver(sudoku.prepare_sudoku_to_solve())

my_sudoku.solve()
print(my_sudoku.board)