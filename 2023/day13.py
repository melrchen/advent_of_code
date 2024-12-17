"""
--- Day 13: Point of Incidence ---
"""

def find_reflection_line(rows, to_ignore): 
    # the to_ignore is a tuple of previously found line of reflection to ignore
    # only used in part 2 

    for i in range(len(rows)-1):
        if i!=to_ignore[0]: 
            # check if line is between i and i+1 
            len_reflection = min(i+1, len(rows)-i-1)
            valid_reflection = True
            for j  in range(len_reflection): 
                if rows[i-j] != rows[i+1+j]:
                    valid_reflection = False 
                    break
            if valid_reflection: 
                return i+1, -1
    
    for i in range(len(rows[0])-1):
        if i!=to_ignore[1]: 
            len_reflection = min(i+1, len(rows[0])-i-1)
            valid_reflection = True
            for j  in range(len_reflection): 
                col1 = [row[i-j] for row in rows]
                col2 = [row[i+1+j] for row in rows]
                if col1 != col2:
                    valid_reflection = False 
                    break
            if valid_reflection: 
                return -1, i+1
    return -1, -1


if __name__=="__main__": 
    input = open("day13input.txt", "r")
    content = input.read()
    grids = content.split("\n\n")
    input.close()

    # it seems we can assume there is one line of reflection in each pattern 

    row_count = 0
    column_count = 0
    grid_lines = []
    for grid in grids: 
        rows = grid.split("\n")
        row, col = find_reflection_line(rows, (-1,-1))
        grid_lines.append((row-1,col-1))
        if row > 0: 
            row_count += row
        if col > 0: 
            column_count += col
    
    print("part1: ", 100*row_count + column_count)

    # for part 2, we can try fixing each smudge and validating if it creates a new line 

    new_row_count = 0
    new_col_count = 0
    for num, grid in enumerate(grids): 
        new_line_found = False
        rows = grid.split("\n")
        # for each cell in grid, flip from . to # or # to .
        for r in range(len(rows)): 
            for c in range(len(rows[0])): 
                new_grid = rows.copy()
                if new_grid[r][c]==".": 
                    new_grid[r] = new_grid[r][:c]+"#"+new_grid[r][c+1:]
                else: 
                    new_grid[r] = new_grid[r][:c]+"."+new_grid[r][c+1:]
                
                row, col = find_reflection_line(new_grid, grid_lines[num])
                if row > -1: 
                    new_row_count+= row 
                    new_line_found = True 
                    break
                elif col > -1: 
                    new_col_count+= col 
                    new_line_found = True
                    break
            if new_line_found: 
                break
    
    print("part 2: ", 100*new_row_count + new_col_count)
