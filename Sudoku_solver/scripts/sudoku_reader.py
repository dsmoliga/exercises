class SudokuReader:
    def __init__(self, file_name: str):
        if type(file_name) is not str:
            raise TypeError('Expected string')
        else:
            self.file_name = file_name
    
    def prepare_sudoku_to_solve(self):
        try:
            with open(self.file_name, 'r', encoding='UTF-8') as file:
                self.content = file.readlines()
                self.content = [list(line.replace('\n', '')) for line in self.content]
                self.content = list(filter(None, self.content))
                number_of_elements = sum([len(list_element) for list_element in self.content])
                if  len(self.content) and number_of_elements is 81:
                    self.content = [[int(digit.replace('.', '0')) for digit in list] for list in self.content]
                    return self.content
                else:
                    raise ValueError('Sudoku is incomplete')
        except FileNotFoundError:
            raise FileNotFoundError(f'{self.file_name} does not exist')
    
    def __len__(self):
        return len(self.content)