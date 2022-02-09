#09.01.2022
#empty-field = incemtenal
#player 1 = XX
#player 2 = OO
#win = in horizontal or vertical

def gen_grid(rows, columns):
    index = 1
    grid = []
    for i in range(rows):
        temp_line = []
        for j in range(rows):
            if index < 10:
                filler = "0"
            else:
                filler = ""
            temp_line.append(filler+str(index))
            index += 1
        grid.append(temp_line)
    return grid

def print_grid(grid):
    separator_int = len(grid)+len(grid*2)
    separator = separator_int*"="
    print(separator)
    for grid_line in grid:
        for grid_line_singel in grid_line:
            print(grid_line_singel, end="|")
        print("\n"+separator)
    return True

def check_horizontal(grid, minimum_win):
    new_indicator = ""
    old_indicator = ""
    
    for grid_line in grid:
        for grid_line_singel in grid_line:
            new_indicator = grid_line_singel
            if (old_indicator == new_indicator):
                char_counter += 1
                if(char_counter == minimum_win-1):
                    return True
            else:
                char_counter = 0
            old_indicator = grid_line_singel
    return False

def check_vertical(grid, minimum_win):
    transpose_grid = []
    for i in range(len(grid[0])):
        row =[]
        for item in grid:
            row.append(item[i])
        transpose_grid.append(row)

    grid = transpose_grid
    new_indicator = ""
    old_indicator = ""
    
    for grid_line in grid:
        for grid_line_singel in grid_line:
            new_indicator = grid_line_singel
            if (old_indicator == new_indicator):
                char_counter += 1
                if(char_counter == minimum_win-1):
                    return True
            else:
                char_counter = 0
            old_indicator = grid_line_singel
    return False

def check_win(grid, minimum_win):
    if(check_vertical(grid, minimum_win) or check_horizontal(grid, minimum_win)):
        return True
    else:
        return False
        
def set_fild(grid, user_index, input_char):
    x = -1
    y = -1
    for grid_line in grid:
        x += 1
        for grid_line_singel in grid_line:
            y += 1
            if (user_index == grid_line_singel):
                grid[x][y] = input_char
                return grid
        y = -1
    return False

def main():
    rows = int(input("how many rows? :"))
    columns = int(input("how many columns? :"))
    grid = gen_grid(rows, columns)
    
    minimum_win = int(input("minimum win [3]: "))
    
    print(5*"*NEW GAME*")
    while True:
        print_grid(grid)
        user_index = str(input("P1-X: selcet the Index: "))
        set_fild(grid, user_index, 'XX')
        if check_win(grid, minimum_win):
            print_grid(grid)
            print("you have won!")
            return True

        print_grid(grid)
        user_index = str(input("P2-0: selcet the Index: "))
        set_fild(grid, user_index, 'OO')
        if check_win(grid, minimum_win):
            print_grid(grid)
            print("you have won!")
            return True


if __name__ == "__main__":
    while True:
        main()
    exit(0)
