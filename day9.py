"""
--- Day 9: Mirage Maintenance ---
"""
def is_zeroes(layer): 
    for i in layer: 
        if i != 0: 
            return False
    return True

def extrapolate_values(history): 
    layers = {}
    layers[0] = history
    curr_layer = 0 
    while not is_zeroes(layers[curr_layer]):
        curr_layer +=1 
        layers[curr_layer] = []
        last_layer = layers[curr_layer-1]
        for i in range(len(last_layer)-1):
            layers[curr_layer].append(last_layer[i+1] - last_layer[i])
    
    curr_layer -= 1

    while curr_layer >= 0:
        layers[curr_layer].append(layers[curr_layer][-1]+layers[curr_layer+1][-1])
        pre = layers[curr_layer][0] - layers[curr_layer+1][0]
        layers[curr_layer].insert(0, pre)
        curr_layer -=1
    
    return layers[0][0], layers[0][-1]
    


if __name__=="__main__": 
    input = open("day9input.txt", "r")
    content = input.read()
    lines = content.split("\n")
    input.close()

    histories = []
    for line in lines: 
        strings = line.split()
        histories.append([eval(x) for x in strings])

    last_value_sum = 0
    first_value_sum = 0

    for history in histories: 
        first_value, last_value = extrapolate_values(history)
        last_value_sum += last_value 
        first_value_sum += first_value
    
    print("part 1: ", last_value_sum)
    print("part 2: ", first_value_sum)
