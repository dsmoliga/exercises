class SudokuReader:
    def __init__(self, file_name: str):
        self.file_name = file_name
    
    def prepare_sudoku_to_solve(self):
        try:
            with open(self.file_name, 'r', encoding='UTF-8') as file:
                self.content = file.readlines()
                self.content = [list(line.replace('\n', '')) for line in self.content] 
                self.content = [[int(digit.replace('.', '0')) for digit in list] for list in self.content]
                return self.content
        except FileNotFoundError:
            print(f'{self.file_name} does not exist.')
    
    def __len__(self):
        return len(self.content)