from sodoku import Sodoku

def import_data():
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
    for row in grid:
        for number in row:
            print(number, end=" ")
        print()

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



