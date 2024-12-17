"""
--- Day 2: Cube Conundrum ---
"""

def clean_color_name(color): 
    if color[-1] == ",": 
        return color[:-1]
    return color

if __name__=="__main__": 
    input = open("day2input.txt", "r")
    content = input.read()
    entries = content.split("\n")
    input.close()

    game_number_sum = 0
    game_power_sum = 0

    for e in entries:
        # get game number 
        game = e.split(":")
        game_number = int(game[0].split()[1])

        # get max count per color
        max_counts = {}
        sets = game[1].split(";")
        for set in sets: 
            colors = set.split()
            for i in range(len(colors)//2):
                count = int(colors[2*i])
                color = clean_color_name(colors[2*i+1])
                if count > max_counts.get(color, 0):
                    max_counts[color] = count
   
        if max_counts.get("blue", 0) <= 14 and max_counts.get("green", 0) <=13 and max_counts.get("red", 0) <= 12:   
            game_number_sum+=game_number
        
        power = 1
        for count in max_counts.values(): 
            power = power*count
        game_power_sum += power

    print(game_number_sum)
    print(game_power_sum)








