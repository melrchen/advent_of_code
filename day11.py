"""
--- Day 11: Cosmic Expansion ---
"""

if __name__=="__main__": 
    input = open("day11input.txt", "r")
    content = input.read()
    grid = content.split("\n")
    input.close()

    # rewriting an approach that works for part 1 and part 2 performantly 

    galaxies = []
    for r in range(len(grid)):
        for c in range(len(grid[0])): 
            if grid[r][c]=='#':
                galaxies.append((r,c))

    galaxy_rows = set(g[0] for g in galaxies)
    empty_rows = sorted(set(range(len(grid))).difference(galaxy_rows))
    galaxy_cols = set(g[1] for g in galaxies)
    empty_cols = sorted(set(range(len(grid[0]))).difference(galaxy_cols))

    part1 = 0
    part2 = 0
    old_multiplier = 999999
    
    # iterate through each pair of galaxies 
    for i in range(len(galaxies)): 
        for j in range(i+1, len(galaxies)):
            g1, g2 = galaxies[i], galaxies[j]
            rows_to_add = len([row for row in empty_rows if g1[0] < row < g2[0] or g2[0] < row < g1[0]])
            cols_to_add = len([col for col in empty_cols if g1[1] < col < g2[1] or g2[1] < col < g1[1]])
            part1 += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) + rows_to_add + cols_to_add
            part2 += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) + old_multiplier*(rows_to_add+cols_to_add)
    
    print("part1: ", part1)
    print("part2: ", part2)

    ######## PART 1 #############

    # expand the universe 
    
    # find indices of rows to expand 
    # grid = original_grid.copy()
    # row_indices = []
    # for row in range(len(grid)):
    #     if grid[row].count('.')==len(grid[row]):
    #         row_indices.append(row)
    # # find indices of columns to expand
    # col_indices = []
    # for col in range(len(grid[0])):
    #     column = [grid[i][col] for i in range(len(grid))]
    #     if column.count('.')==len(column):
    #         col_indices.append(col)
    # # expand rows 
    # for i in range(len(row_indices)): 
    #     grid.insert(row_indices[i]+i, '.'*len(grid[0]))
    # # expand columns 
    # for i in range(len(col_indices)): 
    #     for j in range(len(grid)): 
    #         grid[j] = grid[j][:i+col_indices[i]]+'.'+grid[j][i+col_indices[i]:]
    


    # # find sum of lengths of shortest paths between each galaxy 
            
    # # find each galaxy 
            
    # galaxies = []
    # for r in range(len(grid)): 
    #     for c in range(len(grid[0])):
    #          if grid[r][c] == '#':
    #              galaxies.append((r,c))
    # print(galaxies)
    # # sum shortest distances 
    # sum_shortest_distances = 0 

    # for i in range(len(galaxies)): 
    #     for j in range(i+1, len(galaxies)): 
    #         if i == j: 
    #             continue 
    #         sum_shortest_distances+= abs(galaxies[i][0]-galaxies[j][0])+abs(galaxies[i][1] - galaxies[j][1])

    # print("part 1: ", sum_shortest_distances)
