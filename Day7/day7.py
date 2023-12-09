from functools import cmp_to_key

sorting_key = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7,
               '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}

sorting_key_2 = {'A': 12, 'K': 11, 'Q': 10, 'T': 9, '9': 8,
                 '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, 'J': 0}


def return_type_rank(cards, remove_joker=False):
    ''' Returns the rank of a given hand of cards '''
    cards_string = ''.join(cards)

    if remove_joker:
        joker_count = cards_string.count("J")
        cards = list(filter(lambda a: a != 'J', cards))
    else:
        joker_count = 0

    unique_cards = len(set(cards))
    cards_string = ''.join(cards)

    # all five cards have the same label
    if len(cards) == 0 or unique_cards == 1:
        return 7
    elif unique_cards == 2:
        # Four of a kind: where four cards have the same label and one card has a different label
        for char in cards_string:
            if cards_string.count(char) == 4-joker_count:
                return 6
        # Full house: here three cards have the same label, and the remaining two cards share a different label
        return 5
    elif unique_cards == 3:
        # Three of a kind: three cards have the same label, and the remaining two cards are each different from any other card in the hand
        for char in cards_string:
            if cards_string.count(char) == 3-joker_count:
                return 4
        # Two pair: two cards share one label, two other cards share a second label, and the remaining card has a third label
        return 3
    # One pair: two cards share one label, all three other cards have a different label from the pair and each other
    elif unique_cards == 4:
        return 2
    # High card: all cards have different values -> 1
    elif unique_cards == 5:
        return 1
    else:
        print("error ", cards)


def compare_two_cards_1(card1, card2):
    for i in range(0, len(card1)):
        if card1[i] != card2[i]:
            if sorting_key[card1[i]] < sorting_key[card2[i]]:
                return -1
            else:
                return 1


def compare_two_cards_2(card1, card2):
    for i in range(0, len(card1)):
        if card1[i] != card2[i]:
            if sorting_key_2[card1[i]] < sorting_key_2[card2[i]]:
                return -1
            else:
                return 1


def get_sorted_hands(hands_list, sorting):
    if len(hands_list) > 0:
        if len(hands_list) == 1:
            return ([hands_list[0]])
        else:
            if sorting == 1:
                return sorted(hands_list, key=cmp_to_key(
                    compare_two_cards_1))
            else:
                return sorted(hands_list, key=cmp_to_key(
                    compare_two_cards_2))
    else:
        return ([])


input_file = open("Day7/input1.in", encoding="utf-8")

game_list = {}
hand_list = []

for line in input_file:
    input_array = line.strip().split(" ")
    game_list[input_array[0]] = input_array[1]
    hand_list.append(input_array[0])

ranking_1 = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
ranking_2 = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
for hand in hand_list:
    ranking_1[return_type_rank(hand)].append(hand)
    ranking_2[return_type_rank(hand, True)].append(hand)

ordered_hands_1 = []
ordered_hands_2 = []
for i in range(1, 8):
    hands_1 = ranking_1[i]
    hands_2 = ranking_2[i]
    ordered_hands_1 = ordered_hands_1 + \
        get_sorted_hands(hands_1, 1)
    ordered_hands_2 = ordered_hands_2 + \
        get_sorted_hands(hands_2, 2)

rank = 1
result_1 = 0
for hand in ordered_hands_1:
    result_1 += int(game_list[hand]) * rank
    rank += 1

print("Result 1", result_1)

result_2 = 0
rank = 1
for hand in ordered_hands_2:
    result_2 += int(game_list[hand]) * rank
    rank += 1

print("Result 2", result_2)
