import pytest
import sys
sys.path.append('E:\Projects\Learning_Python\Sudoku_solver')
from scripts.sudoku_reader import SudokuReader

def test_sudoku_reader_init_with_numbers():
    with pytest.raises(TypeError):
        my_sudoku = SudokuReader(123)

def test_sudoku_with_invalid_file_name():
    my_sudoku = SudokuReader('test')
    with pytest.raises(FileNotFoundError):
        my_sudoku.prepare_sudoku_to_solve()
