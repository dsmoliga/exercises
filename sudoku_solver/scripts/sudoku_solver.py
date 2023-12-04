class SudokuSolver:
    def __init__(self, content: list[list]):
        self.board = content
    
    def find_empty_cell(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
        return None

    def valid(self, number, row, col):
        for valid_col in range(9):
            if self.board[row][valid_col] == number and col != valid_col:
                return False
        
        for valid_row in range(9):
            if self.board[valid_row][col] == number and row != valid_row:
                return False
            
        self.box_row = col // 3
        self.box_col = row // 3
        for valid_row in range(self.box_col * 3, self.box_row * 3 + 3):
            for valid_col in range(self.box_row * 3, self.box_col * 3 + 3):
                if self.board[valid_row][valid_col] == number and (valid_row, valid_col) != (row, col):
                    return False
        return True

    def solve(self):
        self.find = self.find_empty_cell()
        if not self.find:
            return True
        else:
            row, col = self.find
        
        for i in range(1,10):
            if self.valid(i, row, col):
                self.board[row][col] = i

                if self.solve():
                    return True
                
                self.board[row][col] = 0
        return False
