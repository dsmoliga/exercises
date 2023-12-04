from scripts.sudoku_reader import SudokuReader
from scripts.sudoku_solver import SudokuSolver
from scripts.sudoku_writer import SudokuWriter

sudoku = SudokuReader('sudoku.txt')
sudoku_solved = SudokuSolver(sudoku.prepare_sudoku_to_solve())
sudoku_solved.solve()
sudoku_write = SudokuWriter(sudoku_solved.board)
sudoku_write.writing_sudoku_to_file()
