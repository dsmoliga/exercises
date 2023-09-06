class SudokuSolver:
    def __init__(self, content: list[list]):
        self.board = content
    
    def find_empty_cell(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    def valid(self, number, position):
        for col in range(9):
            if self.board[position[0]] [col] == number and position[1] != col:
                return False
        
        for row in range(9):
            if self.board[row][position[1]] == number and position[0] != row:
                return False
            
        self.box_row = position[1] // 3
        self.box_col = position[0] // 3
        for row in range(self.box_col * 3, self.box_row * 3 + 3):
            for col in range(self.box_row * 3, self.box_col * 3 + 3):
                if self.board[row][col] == number and (row, col) != position:
                    return False
        return True

    def solve(self):
        self.find = self.find_empty_cell()
        if not self.find:
            return True
        else:
            row, col = self.find
        
        for i in range(1,10):
            if self.valid(i, (row, col)):
                self.board[row][col] = i

                if self.solve():
                    return True
                
                self.board[row][col] = 0
        return False
