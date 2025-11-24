class Sodoku():
        """Sudoku validator class with grid validation methods"""
        def __init__(self, grid):
            """Initialize with sudoku grid"""
            self.grid = grid

        def check_row(self, row, number):
            """Check if number can be placed in specified row"""
            for col in range(9):
                if self.grid[row][col] == number:
                    return False
            return True
            
        def check_column(self, col, number):
            """Check if number can be placed in specified column"""
            for row in range(9):
                if self.grid[row][col] == number:
                    return False
            return True
            
        def check_box(self, row, col, number):
            """Check if number can be placed in 3x3 box"""
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for i in range(3):
                for j in range(3):
                   if self.grid[start_row + i][start_col + j] == number:
                       return False
            return True
        
        def is_valid(self,row, col, number):
            """Validate if number can be placed at given position"""
            return (self.check_row(row, number) and  self.check_column(col, number) and self.check_box(row, col, number))
