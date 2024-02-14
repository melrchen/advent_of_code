"""
--- Day 16: The Floor Will Be Lava ---
"""

# start will be (position, direction)
def count_energized(grid, start): 
    right = (0,1)
    down = (1,0)
    left = (0,-1) 
    up = (-1,0)

    paths = [start]
    seen = set()

    while paths:
        path = paths.pop(0)
        dir = path[1]
        row = path[0][0] + dir[0]
        col = path[0][1] + dir[1]

        # stop checking path if out of bounds
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]): 
            continue 
        
        position = (row, col)
        tile = grid[row][col]
        new_paths = []

        match tile: 
            case ".": 
                new_paths.append((position, dir))
            case "-": 
                if dir[0]==0: 
                    new_paths.append((position, dir))
                else: 
                    new_paths.append((position, right))
                    new_paths.append((position, left))
            case "|": 
                if dir[1]==0: 
                    new_paths.append((position, dir))
                else: 
                    new_paths.append((position, up))
                    new_paths.append((position, down))
            case "\\":
                match dir:
                    case (-1, 0): 
                        new_paths.append((position, left))
                    case (1, 0): 
                        new_paths.append((position, right))
                    case (0, 1): 
                        new_paths.append((position, down))
                    case (0, -1): 
                        new_paths.append((position, up))
            case "/":
                match dir:
                    case (-1, 0): 
                        new_paths.append((position, right))
                    case (1, 0): 
                        new_paths.append((position, left))
                    case (0, 1): 
                        new_paths.append((position, up))
                    case (0, -1): 
                        new_paths.append((position, down))
        
        for new_path in new_paths: 
            if new_path not in seen: 
                seen.add(new_path)
                paths.append(new_path)

    energized = {(r,c) for ((r,c), (_,_)) in seen}
    return len(energized)


if __name__=="__main__": 
    input = open("day16input.txt", "r")
    grid = input.read().splitlines()
    input.close()

   # part 1

    print("part 1: ", count_energized(grid, ((0,-1), (0,1))))

    # part 2 
    # check any possible entrance point 

    max_energized = 0

    # right left entry
    for r in range(len(grid)): 
        left = count_energized(grid, ((r, -1), (0,1)))
        right = count_energized(grid, ((r, len(grid[0])), (0, -1)))
        max_energized = max(left, right, max_energized)
    
    # up down entry 
    for c in range(len(grid[0])):
        up = count_energized(grid, ((len(grid), c), (-1, 0)))
        down = count_energized(grid, ((-1, c), (1, 0)))
        max_energized = max(up, down, max_energized)
    
    print("part 2: ", max_energized)


        

