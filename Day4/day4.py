
from functools import reduce

input = open("Day4/input1.in")

result_1 = 0

win_map_1 = {}
win_map_2 = {}
card_map = {}

for line in input:
    card_id = int(line.split(":")[0].replace("Card ", "").strip())
    line = line.replace("  ", " ")
    line = line.split(":")[1]
    winning = line.split("|")[0].strip().split(" ")
    cards = line.split("|")[1].strip().split(" ")

    line_result = 0
    winning_cards = 0

    if card_id in win_map_2:
        win_map_2[card_id] = win_map_2[card_id]+1
    else:
        win_map_2[card_id] = 1

    for card in cards:
        if card in winning:
            winning_cards = winning_cards + 1
            if line_result == 0:
                line_result = line_result+1
            else:
                line_result = line_result*2

    win_map_1[card_id] = line_result

    for copy in range(card_id+1, card_id+winning_cards+1):
        if copy in win_map_2:
            win_map_2[copy] = win_map_2[copy]+win_map_2[card_id]
        else:
            win_map_2[copy] = win_map_2[card_id]
    result_1 = result_1 + line_result

print("result 1: ", reduce(lambda a, b: int(a) + int(b), win_map_1.values()))

result_2 = 0

for card in win_map_2:
    if card in win_map_1:
        result_2 = result_2 + win_map_2[card]

print("result 2 ", result_2)
