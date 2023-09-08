import pytest
from unittest import mock
import builtins
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

def test_prepare_sudoku_to_solve_with_incomplete_board():
    with pytest.raises(ValueError):
        my_sudoku = SudokuReader('sudoku.txt')
        my_sudoku.prepare_sudoku_to_solve()


test_board = """9.....268
168.7a.4.
......1..
..7......
3....76.1
..62.4..3
4.3...79.
.2....83.
........4"""

test_outcome = [[9, 0, 0, 0, 0, 0, 2, 6, 8], 
                [1, 6, 8, 0, 7, 0, 0, 4, 0], 
                [0, 0, 0, 0, 0, 0, 1, 0, 0], 
                [0, 0, 7, 0, 0, 0, 0, 0, 0], 
                [3, 0, 0, 0, 0, 7, 6, 0, 1], 
                [0, 0, 6, 2, 0, 4, 0, 0, 3], 
                [4, 0, 3, 0, 0, 0, 7, 9, 0], 
                [0, 2, 0, 0, 0, 0, 8, 3, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 4]]

@mock.patch.object(builtins, 'open', new_callable=mock.mock_open, read_data=test_board)
def test_file_read_with_letter(mock_file_open):
    with pytest.raises(ValueError):
        my_sudoku = SudokuReader('sudoku.txt')
        my_sudoku.prepare_sudoku_to_solve()
