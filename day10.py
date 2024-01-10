"""
--- Day 10: Pipe Maze ---
"""

def find_indices(row):
    indices = []
    for i, x in enumerate(row): 
        if x==1: 
            indices.append(i)
    return indices      

if __name__=="__main__": 
    input = open("day10input.txt", "r")
    content = input.read()
    grid = content.split("\n")
    input.close()

    # first find S, the starting point 
    
    for r in range(len(grid)): 
        for c in range(len(grid[r])): 
            if grid[r][c]=='S': 
                start_y, start_x = r, c

    x, y, steps = start_x, start_y, 0
    if y > 1 and grid[y - 1][x] in {'|', 'F', '7'}:
        direction = 0 # up 
    elif x < len(grid[0]) - 1 and grid[y][x + 1] in {'-', 'J', '7'}:
        direction = 1 # right 
    elif y < len(grid) - 1 and grid[y + 1][x] in {'|', 'J', 'L'}:
        direction = 2 # down
    elif x > 0 and grid[y][x - 1] in {'-', 'F', 'L'}:
        direction = 3 #left 
    
    pipe = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    pipe[y][x] = 1
    while True:
        match direction:
            case 0:
                y -= 1
            case 1:
                x += 1
            case 2:
                y += 1
            case 3:
                x -= 1
        match grid[y][x]:
            case 'L':
                direction = 1 if direction == 2 else 0
            case 'J':
                direction = 3 if direction == 2 else 0
            case '7':
                direction = 2 if direction == 1 else 3
            case 'F':
                direction = 2 if direction == 3 else 1
        steps += 1
        print("y: ", y, "x: ", x)
        pipe[y][x] = 1
        if start_x == x and start_y == y:
            print("part 1: ", steps // 2 + (1 if steps % 2 == 1 else 0))
            break
    

    # hm i may have misunderstood this one. flood filling? ray tracing? punting for a bit
    count = 0 
    for row in pipe:
        pipe_indices = find_indices(row)
        for i in range(len(pipe_indices)//2):
            count += pipe_indices[2*i+1] - pipe_indices[2*i]-1
    print("part 2: ", count)