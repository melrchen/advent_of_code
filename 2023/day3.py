"""
--- Day 3: Gear Ratios ---
"""

# we mutate the grid in this function so we don't double count part numbers
def fetch_num(grid, x, y): 
    row = grid[x]
    leftindex = -1
    rightindex = -1
    leftplacer = y
    rightplacer = y
    while leftindex < 0 or rightindex < 0: 
        if leftplacer - 1 < 0 or not row[leftplacer-1].isnumeric():
            leftindex = leftplacer
        else: 
            leftplacer-=1
        if rightplacer + 1 == len(row) or not row[rightplacer+1].isnumeric(): 
            rightindex = rightplacer
        else: 
            rightplacer +=1
    part_number = int(row[leftindex: rightindex+1])
    grid[x] = row[:leftindex] + '.'*(rightindex-leftindex+1) + row[rightindex+1:]
    return part_number
    

def fetch_sum(grid, x, y): 
    sum = 0
    directions = [(0,1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for dir in directions: 
        newx = x+dir[0]
        newy = y+dir[1]

        # check that newx and newy are valid
        if newx < 0 or newx >= len(grid) or newy < 0 or newy >= len(grid[0]):
            continue 
        
        if grid[newx][newy].isnumeric():
            sum+= fetch_num(grid, newx, newy)

    return sum

def fetch_gear_ratio(grid, x, y): 
    gear_ratio = 0 
    part_nums = []
    directions = [(0,1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for dir in directions: 
        newx = x+dir[0]
        newy = y+dir[1]

        # check that newx and newy are valid
        if newx < 0 or newx >= len(grid) or newy < 0 or newy >= len(grid[0]):
            continue 
        
        if grid[newx][newy].isnumeric():
            part_nums.append(fetch_num(grid, newx, newy))
    
    if len(part_nums) == 2: 
        gear_ratio = part_nums[0] * part_nums[1]
    return gear_ratio


def is_special(s): 
    return s in "!@#$%^&*()-+?_=,<>/"

if __name__=="__main__": 
    input = open("day3input.txt", "r")
    content = input.read()
    grid = content.split("\n")
    input.close()

    # sum = 0
    gear_ratio_sum = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # if is_special(grid[row][col]): 
            #     sum+=fetch_sum(grid, row, col)
            if grid[row][col] == '*':
                gear_ratio_sum += fetch_gear_ratio(grid, row, col)
    
    # print("part 1: ", sum)
    print("part 2: ", gear_ratio_sum)
