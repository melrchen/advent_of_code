"""
--- Day 17: Clumsy Crucible ---
"""

from heapq import heappop, heappush

dirs = {0: (-1,0), 1: (0,1), 2: (1,0), 3: (0, -1)}

def go_straight(loc, dir, grid): 
    new_loc = (loc[0]+dirs[dir][0], loc[1]+dirs[dir][1])
    if new_loc in grid:
        return new_loc, dir
    return None

def rotate_right(loc, dir, grid): 
    new_dir = (dir+1)%4
    new_loc = (loc[0]+dirs[new_dir][0], loc[1]+dirs[new_dir][1])
    if new_loc in grid:
        return new_loc, new_dir
    return None

def rotate_left(loc, dir, grid): 
    new_dir = (dir-1)%4
    new_loc = (loc[0]+dirs[new_dir][0], loc[1]+dirs[new_dir][1])
    if new_loc in grid:
        return new_loc, new_dir
    return None

def get_min_cost(grid, min_steps, max_steps):
    target = (140, 140)
    seen = set()
    paths = [(0, (0, 0), 2, 0), (0, (0, 0), 1, 0)]

    while paths:
        cost, loc, dir, num_steps = heappop(paths)
        if loc==target and num_steps >= min_steps:
            return cost 
        if (loc, dir, num_steps) in seen: 
            continue 
        seen.add((loc, dir, num_steps))

        # can either go straight, left, or right
        if num_steps < max_steps and go_straight(loc, dir, grid): 
            next_step, next_dir = go_straight(loc, dir, grid)
            heappush(paths, (cost+grid[next_step], next_step, next_dir, num_steps+1))
        if num_steps >= min_steps and rotate_left(loc, dir, grid):
            next_step, dir = rotate_left(loc, dir, grid)
            heappush(paths, (cost+grid[next_step], next_step, next_dir, 1))
        if num_steps >= min_steps and rotate_right(loc, dir, grid):
            next_step, dir = rotate_right(loc, dir, grid)
            heappush(paths, (cost+grid[next_step], next_step, next_dir, 1))

if __name__=="__main__": 
    input = open("day17input.txt", "r")
    content = input.read().splitlines()
    input.close()
    grid = {}
    for r in range(len(content)): 
        for c in range(len(content[0])): 
            grid[(r,c)] = int(content[r][c])
    print("part 1: ", get_min_cost(grid, 0, 3))
    print("part 2: ", get_min_cost(grid, 4, 10))
    



