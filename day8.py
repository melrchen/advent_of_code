"""
--- Day 8: Haunted Wasteland ---
"""

import re
from functools import reduce 
from math import lcm 

ROUTE="LRRLRRLRLLLRLLRLRRLRRLRRLRRLLRLLRRRLRRRLRRLLLRLRRLLLLLRRRLRRRLRRRLRRLRRLRLRLRLRLRRRLRRRLRRRLRRLRRLRLRLRRLLRRRLLRRLRRLRRRLRLLRRLRRLRRRLRRRLRRRLRRRLRRLLLRRRLLRRLLLRRLRRLLRRLRRRLRRLRRLRRRLRRLLLRLRRRLLRRRLRLRRLRLRLRLRRRLRLRLRRLLRRLRRLRRLRRLLRLRLRRRLRRLRRLRRLRLRRRLRRLRLLRRLLRRLRLLLRLLRRRLRLRLLRRRR"

if __name__=="__main__": 
    input = open("day8input.txt", "r")
    content = input.read()
    nodes = content.split("\n")
    input.close()

    # part 1 

    # # we construct a map with node: (left_child, right_child)
    # map = {}

    # for node in nodes:
    #     # match groupings of 3 capital letters
    #     node_names = re.findall(r'\b[A-Z]{3}\b', node)
    #     map[node_names[0]] = node_names[1:]

    # # we follow the steps in the route starting from 'AAA' until we reach 'ZZZ'
    # num_steps = 0 
    # curr_position = 'AAA'
    # route_index = 0

    # while curr_position != 'ZZZ':
    #     next_steps = map[curr_position]
    #     if ROUTE[route_index]=='L':
    #         curr_position = next_steps[0]
    #     else: 
    #         curr_position = next_steps[1]
    #     num_steps += 1 
    #     route_index += 1
    #     # loop back over if we hit the end of instructions
    #     if route_index==len(ROUTE): 
    #         route_index = 0 
    
    # print("found ZZZ in", num_steps, "steps")

    # part 2 

    # we construct a map with node: (left_child, right_child)
    map = {}
    starting_nodes = []

    for node in nodes:
        # match groupings of 3 capital letters
        node_names = re.findall(r'\b[A-Z]{3}\b', node)
        map[node_names[0]] = node_names[1:]
        if node_names[0][2]=='A':
            starting_nodes.append(node_names[0])

    # we follow the steps in the route starting from '__A''s until we hit all '__Z''s
    # once we have the num_steps for each starting node, we find the LCM of all the num_steps
    steps = []

    for i in range(len(starting_nodes)): 
        curr_position = starting_nodes[i]
        num_steps = 0 
        route_index = 0
        while curr_position[2] != 'Z':
            next_steps = map[curr_position]
            if ROUTE[route_index]=='L':
                curr_position = next_steps[0]
            else: 
                curr_position = next_steps[1]
            num_steps += 1 
            route_index += 1
            # loop back over if we hit the end of instructions
            if route_index==len(ROUTE): 
                route_index = 0
        steps.append(num_steps)

    part_2_steps = reduce(lcm, steps)
    
    print("found all Z's in", part_2_steps, "steps")
        


