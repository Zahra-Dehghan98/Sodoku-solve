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

        
