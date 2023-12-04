from functools import reduce

input_file = open("Day4/input1.in", encoding="utf-8")

RESULT_1 = 0

win_map_1 = {}
win_map_2 = {}
card_map = {}

for line in input_file:
    card_id = int(line.split(":")[0].replace("Card ", "").strip())
    line = line.replace("  ", " ").split(":")[1]
    winning = line.split("|")[0].strip().split(" ")
    cards = line.split("|")[1].strip().split(" ")

    LINE_RESULT = 0
    WINNING_CARDS = 0

    if card_id in win_map_2:
        win_map_2[card_id] = win_map_2[card_id]+1
    else:
        win_map_2[card_id] = 1

    for card in cards:
        if card in winning:
            WINNING_CARDS += 1
            if LINE_RESULT == 0:
                LINE_RESULT += 1
            else:
                LINE_RESULT *= 2

    win_map_1[card_id] = LINE_RESULT

    for copy in range(card_id+1, card_id+WINNING_CARDS+1):
        if copy in win_map_2:
            win_map_2[copy] = win_map_2[copy]+win_map_2[card_id]
        else:
            win_map_2[copy] = win_map_2[card_id]
    RESULT_1 += LINE_RESULT

RESULT_2 = 0

for card, card_count in win_map_2.items():
    if card in win_map_1:
        RESULT_2 = RESULT_2 + card_count

print("Result 1", reduce(lambda a, b: int(a) + int(b), win_map_1.values()))
print("Result 2", RESULT_2)
