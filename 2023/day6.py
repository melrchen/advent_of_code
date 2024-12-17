"""
--- Day 6: Wait For It ---
"""

# [time, distance]
records = [[45, 295], [98, 1734], [83, 1278], [73, 1210]]

records_2 = [45988373, 295173412781210]

# part_1 = 1

# for record in records: 
#     num_ways_to_win = 0
#     for t in range(record[0]): 
#         if t*(record[0]-t) > record[1]: 
#             num_ways_to_win+=1
#     part_1 = part_1 * num_ways_to_win

# print(part_1)

part_2 = 0
for t in range(records_2[0]): 
    if t*(records_2[0]-t) > records_2[1]: 
        part_2+=1
print(part_2)