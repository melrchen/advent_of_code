"""
--- Day 15: Lens Library ---
"""

def get_hash(s): 
    current_value = 0 
    for c in s: 
        current_value += ord(c)
        current_value *= 17 
        current_value = current_value%256
    return current_value

if __name__=="__main__": 
    input = open("day15input.txt", "r")
    content = input.read()
    steps = content.split(",")
    input.close()

    # part 1 

    sum_of_hashes = 0 
    for step in steps: 
        sum_of_hashes += get_hash(step)
    
    print("part 1: ", sum_of_hashes)

    # part 2 

    library = {i: [] for i in range(256)}
    for step in steps: 
        if '=' in step: 
            lens = step.split('=')
            i = get_hash(lens[0])
            found = False
            for j in range(len(library[i])): 
                if library[i][j][0]==lens[0]: 
                    library[i][j] = (lens[0], lens[1])
                    found = True
            if not found: 
                library[i].append((lens[0], lens[1]))
        elif '-' in step: 
            lens = step.split('-')
            i = get_hash(lens[0])
            for j in range(len(library[i])):
                if library[i][j][0]==lens[0]: 
                    library[i].pop(j)
                    break
    # focusing power = (1+box_number) * (slot number) * (focal length)
    
    focusing_power = 0
    for i in range(256): 
        for j in range(len(library[i])): 
            focusing_power+= (i+1) * (j+1) * int(library[i][j][1])
    
    print("part 2: ", focusing_power)

