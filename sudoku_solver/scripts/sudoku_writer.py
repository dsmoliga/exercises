class SudokuWriter:
    def __init__(self, content):
        self.content = content
    
    def writing_sudoku_to_file(self):
        with open('sudoku_solution.txt', 'w') as file:
            for line in self.content:
                file.write(str(line) + '\n')
