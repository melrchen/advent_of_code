"""
--- Day 7: Camel Cards ---
"""

from functools import cmp_to_key

def get_higher_hand(input1, input2): 
    order = "AKQT98765432J"
    hand1 = input1[0]
    hand2 = input2[0]
    for i in range(5): 
        if hand1[i]!=hand2[i]:
            for char in order: 
                if char==hand1[i]: 
                    return 1
                elif char==hand2[i]:
                    return -1
    return 0

def get_hand_type(hand):
    parsed_hand = {}
    for card in hand: 
        parsed_hand[card] = parsed_hand.get(card, 0)+1
    return parse_hand_type(parsed_hand)

def get_hand_type_with_wildcards(hand):
    parsed_hand = {}
    for card in hand: 
        parsed_hand[card] = parsed_hand.get(card, 0)+1
    lowest_type = parse_hand_type(parsed_hand)
    if parsed_hand.get('J', 0) > 0: 
        for c in parsed_hand.keys():
            if c == 'J':
                continue
            new_hand = parsed_hand.copy()
            new_hand[c] = new_hand.get(c, 0)+new_hand['J']
            del(new_hand['J'])
            new_type = parse_hand_type(new_hand) 
            if new_type < lowest_type: 
                lowest_type = new_type
    return lowest_type

def parse_hand_type(parsed_hand):
    counts = sorted(parsed_hand.values())
    # five of a kind
    if counts==[5]:
        return 0
    # four of a kind
    elif counts==[1, 4]: 
        return 1
    # full house
    elif counts==[2, 3]: 
        return 2
    # three of a kind 
    elif counts==[1, 1, 3]:
        return 3
    # two pair
    elif counts==[1, 2, 2]: 
        return 4
    # one pair 
    elif counts==[1, 1, 1, 2]: 
        return 5
    # high number
    else: 
        return 6
    

if __name__=="__main__": 
    input = open("day7input.txt", "r")
    content = input.read()
    hands = content.split("\n")
    input.close()

    # five of a kind
    # four of a kind
    # full house
    # two pair 
    # one pair 
    # high number 
    hands_by_type = {}
    for i in range(7): 
        hands_by_type[i] = []
    
    # for hand in hands: 
    #     cards = hand.split()
    #     hands_by_type[get_hand_type(cards[0])].append(cards)
    for hand in hands: 
        cards = hand.split()
        hands_by_type[get_hand_type_with_wildcards(cards[0])].append(cards)
    
    sorted_hands = []
    for i in range(7): 
        hands = hands_by_type[6-i]
        hands = sorted(hands, key=cmp_to_key(get_higher_hand))
        sorted_hands.extend(hands)
        print(hands)
    
    total_winnings = 0
    for i in range(len(sorted_hands)):
        total_winnings += int(sorted_hands[i][1])*(i+1)

    print(total_winnings)



    

    

