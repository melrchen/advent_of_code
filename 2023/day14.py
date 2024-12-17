"""
--- Day 14: Parabolic Reflector Dish ---
"""

oneb=1000000000

def tilt_north(p): 
    platform = [[c for c in row] for row in p]
    #north
    for r in range(len(platform)): 
        for c in range(len(platform[0])):
            if platform[r][c]=='O': 
                new_r = r
                while new_r-1 >= 0 and platform[new_r-1][c]=='.': 
                    new_r -= 1 
                platform[r][c]='.'
                platform[new_r][c]='O'
    return platform

def cycle_platform(p): 
    platform = [[c for c in row] for row in p]
    #north
    for r in range(len(platform)): 
        for c in range(len(platform[0])):
            if platform[r][c]=='O': 
                new_r = r
                while new_r-1 >= 0 and platform[new_r-1][c]=='.': 
                    new_r -= 1 
                platform[r][c]='.'
                platform[new_r][c]='O'
    #west 
    for c in range(len(platform[0])): 
        for r in range(len(platform)):
            if platform[r][c]=='O': 
                new_c = c
                while new_c-1 >= 0 and platform[r][new_c-1]=='.': 
                    new_c -= 1 
                platform[r][c]='.'
                platform[r][new_c]='O'
    #south
    for r in range(len(platform)-1, -1, -1): 
        for c in range(len(platform[0])):
            if platform[r][c]=='O': 
                new_r = r
                while new_r+1 < len(platform) and platform[new_r+1][c]=='.': 
                    new_r += 1 
                platform[r][c]='.'
                platform[new_r][c]='O'       
    #east
    for c in range(len(platform[0])-1, -1, -1): 
        for r in range(len(platform)):
            if platform[r][c]=='O': 
                new_c = c
                while new_c+1 < len(platform[0]) and platform[r][new_c+1]=='.': 
                    new_c += 1 
                platform[r][c]='.'
                platform[r][new_c]='O'
    
    return tuple(["".join(row) for row in platform])

if __name__=="__main__": 
    input = open("day14input.txt", "r")
    content = input.read()
    rows = content.split("\n")
    input.close()

    p1_platform = tilt_north(rows)
    
    load = 0
    for i, row in enumerate(p1_platform): 
        load += (len(p1_platform)-i)*row.count('O')
    
    print("part 1: ", load)

    platform = tuple(rows)
    seen = {platform}
    platforms = [platform]
    
    for i in range(oneb):
        platform = cycle_platform(platform)
        if platform in seen: 
            break 
        seen.add(platform)
        platforms.append(platform)

    # cycle could start whenever
    cycle_start = platforms.index(platform)
    cycle_length = i + 1 - cycle_start
    final_platform = platforms[((oneb-cycle_start) % cycle_length)+cycle_start]

    load2 = 0
    for i, row in enumerate(list(final_platform)): 
        load2 += (len(final_platform)-i)*row.count('O')
    
    print("part 2: ", load2)
