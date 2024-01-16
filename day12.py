"""
--- Day 12: Hot Springs ---
"""

def find_num_arrangements(record, checksum):
    print(record)
    print(checksum)
    positions = {0: 1}
    # for each contiguous set of springs in records, we find all the possible starting positions and maintain a sum 
    # of all the possible arrangements thus far that include that starting position
    for i, contiguous in enumerate(checksum):
        print(positions)
        new_positions = {}
        for k, v in positions.items():
            for n in range(k, len(record) - sum(checksum[i + 1:]) + len(checksum[i + 1:])):
                if n + contiguous - 1 < len(record) and '.' not in record[n:n + contiguous]:
                    if (i == len(checksum) - 1 and '#' not in record[n + contiguous:]) or (i < len(checksum) - 1 and n + contiguous < len(record) and record[n + contiguous] != '#'):
                        new_positions[n + contiguous + 1] = new_positions[n + contiguous + 1] + v if n + contiguous + 1 in new_positions else v
                if record[n] == '#':
                    break
        positions = new_positions
    return sum(positions.values())

if __name__=="__main__": 
    input = open("day12input.txt", "r")
    content = input.read()
    rows = content.split("\n")
    input.close()

    part1 = 0 
    part2 = 0
    for row in rows: 
        record, checksum = row.split()
        checksum = [int(n) for n in checksum.split(',')]
        part1 += find_num_arrangements(record, checksum)

        record2 = '?'.join([record for i in range(5)])
        checksum2 = checksum*5
        part2 += find_num_arrangements(record2, checksum2)
    print("part1: ", part1)
    print("part2: ", part2)

