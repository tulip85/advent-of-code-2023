input_file = open("Day3/input1.in", encoding="utf-8")

valid_symbols = ["!", "@", "#", "$", "%", "^", "&", "*",
                 "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "/"]

symbol_pos = []
number_pos = {}
star_pos = []
digit_pos = {}

LINE = 0
POS = 0
MAX_LEN = 0


def is_adjacent_to_symbol(num_line, num_pos, num_length, symbols):
    # generate all possible positions that would qualify as adjacent
    # (doesn't matter if negative or outside vector)
    adj = False
    for l in range(num_line-1, num_line+2):
        for p in range(num_pos-1, num_pos+num_length+1):
            if (l, p) in symbols:
                adj = True
    return adj


def return_gear(num_line, num_pos):
    possible_pos = []
    for l in range(num_line-1, num_line+2):
        for p in range(num_pos-1, num_pos+2):
            if (l, p) in digit_pos and digit_pos[(l, p)] not in possible_pos:
                possible_pos.append(digit_pos[(l, p)])

    if len(possible_pos) == 2:
        gear_ratio = number_pos[possible_pos[0]] * number_pos[possible_pos[1]]
        return gear_ratio
    return 0


# load all the symbol and digit positions
for line_in in input_file:
    POS = 0
    NUM = False
    NUM_STR = ""
    for char in line_in:

        # detect end of number
        if NUM and not char.isdigit():
            number_pos[(LINE, POS-len(NUM_STR))] = int(NUM_STR)
            for i in range(POS-len(NUM_STR), POS):
                digit_pos[LINE, i] = (LINE, POS-len(NUM_STR))
            NUM = False
            NUM_STR = ""

        if char in valid_symbols:
            symbol_pos.append((LINE, POS))
            if char == "*":
                star_pos.append((LINE, POS))
        elif char.isdigit():
            NUM = True
            NUM_STR += char

        POS += 1
    LINE += 1

RESULT_1 = 0
RESULT_2 = 0

has_neighbors = {}
potential_gears = {}

is_next_to_star = {}

# find all numbers which are next to a symbol
for (line, pos) in number_pos:
    LENGTH = len(str(number_pos[(line, pos)]))
    if LENGTH > MAX_LEN:
        MAX_LEN = LENGTH
    if is_adjacent_to_symbol(line, pos, LENGTH, symbol_pos):
        has_neighbors[(line, pos)] = number_pos[(line, pos)]
        RESULT_1 = RESULT_1 + number_pos[(line, pos)]

for (line, pos) in star_pos:
    RESULT_2 = RESULT_2 + return_gear(line, pos)

print("Result 1", RESULT_1)
print("Result 2", RESULT_2)
