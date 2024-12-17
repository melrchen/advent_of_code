"""
--- Day 4: Scratchcards ---
"""

def calculate_score(winning_numbers, numbers_you_have): 
    score = 0

    # store winning_numbers for O(1) lookup through numbers you have
    win_map = {}
    for num in winning_numbers: 
        win_map[num] = 1
    
    for num in numbers_you_have: 
        if win_map.get(num, 0) == 1: 
            if score == 0: 
                score = 1
            else: 
                score = score * 2 

    return score

def find_num_winning_numbers(winning_numbers, numbers_you_have):
    total = 0
    # store winning_numbers for O(1) lookup through numbers you have
    win_map = {}
    for num in winning_numbers: 
        win_map[num] = 1
    
    for num in numbers_you_have: 
        if win_map.get(num, 0) == 1: 
            total+=1
    return total

if __name__=="__main__": 
    input = open("day4input.txt", "r")
    content = input.read()
    lines = content.split("\n")
    input.close()

    sum = 0
    for line in lines: 
        numbers = line.split(":")[1]
        split_numbers = numbers.split("|")
        winning_numbers = split_numbers[0].split()
        numbers_you_have = split_numbers[1].split()
        sum += calculate_score(winning_numbers, numbers_you_have)
    
    print("part 1: ", sum)

    card_count = {}
    
    # initialize card_count with initial set of cards
    for i in range(len(lines)):
        card_count[i+1] = 1
    
    # increment card counts
    for i in range(len(lines)):
        line = lines[i]
        numbers = line.split(":")[1]
        split_numbers = numbers.split("|")
        winning_numbers = split_numbers[0].split()
        numbers_you_have = split_numbers[1].split()
        num_wins = find_num_winning_numbers(winning_numbers, numbers_you_have)
        for j in range(num_wins): 
            card_count[i+j+2] += card_count[i+1]

    # sum total number of cards
            
    # TODO: figure out why the line below is erroring 
    # num_scorecards = sum(card_count.values())
    num_scorecards = 0 
    for i in card_count.values(): 
        num_scorecards+= i 

    print("part 2: ", num_scorecards)



