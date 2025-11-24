#Import Sudoku class
from sodoku import Sodoku

def import_data():
    """Read sudoku puzzle from file and return as 2D grid"""
    with open ("sodoku-data.txt", "r") as file:
        grid = []
        for line in file:
            numbers = []
            lists = line.split()
            for i in lists:
                num = int(i)
                numbers.append(num)
            grid.append(numbers)
        return grid
def sodoku_solve(grid):  
    """Solve sudoku puzzle using backtracking algorithm"""
    sodoku = Sodoku(grid)
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for number in range (1, 10):
                    if sodoku.is_valid(row, col, number):
                        grid[row][col] = number

                        if sodoku_solve(grid):
                            return True
                        grid [row][col] = 0
                return False
    return True

def print_grid(grid):
    """Display sudoku grid in readable format"""
    for row in grid:
        for number in row:
            print(number, end=" ")
        print()

# Main execution
grid = import_data()
print ("unsolved sodoku")
print_grid(grid)
print ("===================")
if sodoku_solve(grid):
    print("solved sodoku")
    print_grid(grid)
    print ("===================")
else:
    print("No solution exists!")



