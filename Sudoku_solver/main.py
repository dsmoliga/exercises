from scripts.get_sudoku import Get_Sudoku

sudoku = Get_Sudoku('sudoku.txt')
sudoku.get_sudoku_from_file()
print(sudoku.prepare_sudoku_to_solve())
