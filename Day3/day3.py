input = open("Day3/input1.in")

valid_symbols = ["!", "@", "#", "$", "%", "^", "&", "*",
                 "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "/"]

symbol_pos = []
number_pos = {}
star_pos = []
digit_pos = {}

line = 0
pos = 0
max_len = 0


def is_adjacent_to_symbol(line, pos, length, symbols):
    # generate all possible positions that would qualify as adjacent (doesn't matter if negative or outside vector)
    pos_adj = []
    for l in range(line-1, line+2):
        for p in range(pos-1, pos+length+1):
            pos_adj.append((l, p))
    adj = False
    for pos_pos in pos_adj:
        if pos_pos in symbols:
            adj = True

    return adj


def return_gear(line, pos):
    neighbor_pos = [(line-1, pos-1), (line-1, pos), (line-1, pos+1), (line, pos-1),
                    (line, pos+1), (line+1, pos-1), (line+1, pos), (line+1, pos+1)]

    possible_pos = []
    for l in range(line-1, line+2):
        for p in range(pos-1, pos+2):
            if (l, p) in digit_pos:
                if digit_pos[(l, p)] not in possible_pos:
                    possible_pos.append(digit_pos[(l, p)])

    number_n = 0

    if len(possible_pos) == 2:
        gear_ratio = number_pos[possible_pos[0]] * number_pos[possible_pos[1]]
        return gear_ratio
    return 0


# load all the symbol and digit positions
for line_in in input:
    pos = 0
    num = False
    num_str = ""
    for char in line_in:

        # detect end of number
        if num and not char.isdigit():
            number_pos[(line, pos-len(num_str))] = int(num_str)
            for i in range(pos-len(num_str), pos):
                digit_pos[line, i] = (line, pos-len(num_str))
            num = False
            num_str = ""

        if char in valid_symbols:
            symbol_pos.append((line, pos))
            if char == "*":
                star_pos.append((line, pos))
        elif char.isdigit():
            num = True
            num_str = num_str + char

        pos = pos+1
    line = line+1

result = 0
result2 = 0

has_neighbors = {}
potential_gears = {}

is_next_to_star = {}

# find all numbers which are next to a symbol
for (line, pos) in number_pos:
    length = len(str(number_pos[(line, pos)]))
    if length > max_len:
        max_len = length
    if is_adjacent_to_symbol(line, pos, length, symbol_pos):
        has_neighbors[(line, pos)] = number_pos[(line, pos)]
        result = result + number_pos[(line, pos)]

for (line, pos) in star_pos:
    result2 = result2 + return_gear(line, pos)

print(result)
print(result2)
