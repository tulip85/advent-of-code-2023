""" Very slow solution, runs in about 3-5 minutes """
from functools import cache
RESULT1 = 0

counter = 0
rock_registry_round = []
rock_registry_square = []

LINE = 0


def compare_maps(map1, map2):
    for j in range(0, LINE):
        for i in range(0, COL):
            if ((j, i) in map1 and (j, i) not in map2) or ((j, i) in map2 and (j, i) not in map1):
                return -1
    return 1


def roll_north(round_rocks, square_rocks):
    blocking_rocks = square_rocks.copy()

    result_array_round = []
    for (l, c) in round_rocks:
        # find the closest square rock with the same column
        stopped = False
        for i in range(l-1, -1, -1):
            if (i, c) in blocking_rocks:
                result_array_round.append((i+1, c))
                blocking_rocks.append((i+1, c))
                stopped = True
                break
        if not stopped:
            result_array_round.append((0, c))
            blocking_rocks.append((0, c))
    return result_array_round


def get_weight(positions):
    result = 0
    for (line, col) in positions:
        result += LINE-line
    return result


def roll(round_rocks, square_rocks, max_rows, max_cols, vertical=-1, horizontal=0):
    blocking_rocks = square_rocks.copy()

    reverse_sort = vertical == 1 or horizontal == 1

    # sort the round rocks according to the direction
    if vertical != 0:
        round_rocks.sort(key=lambda x: x[0], reverse=reverse_sort)
        end = vertical if vertical == -1 else max_rows+1
        default = 0 if vertical == -1 else max_rows-1
    else:
        round_rocks.sort(key=lambda x: x[1], reverse=reverse_sort)
        end = horizontal if horizontal == -1 else max_cols+1
        default = 0 if horizontal == -1 else max_cols-1

    result_array_round = []
    for (l, c) in round_rocks:
        stopped = False
        if vertical != 0:
            for i in range(l+vertical, end, vertical):
                if (i, c) in blocking_rocks:
                    result_array_round.append((i+(-1*vertical), c))
                    blocking_rocks.append((i+(-1*vertical), c))
                    stopped = True
                    break
            if not stopped:
                result_array_round.append((default, c))
                blocking_rocks.append((default, c))
        else:
            for i in range(c+horizontal, end, horizontal):
                if (l, i) in blocking_rocks:
                    result_array_round.append((l, i+(-1*horizontal)))
                    blocking_rocks.append((l, i+(-1*horizontal)))
                    stopped = True
                    break
            if not stopped:
                result_array_round.append((l, default))
                blocking_rocks.append((l, default))
    return result_array_round


for line in open("Day14/input1.in", encoding="utf-8"):
    COL = 0
    for item in line:
        if item == "#":
            rock_registry_square.append((LINE, COL))
        elif item == "O":
            rock_registry_round.append((LINE, COL))
        COL += 1
    LINE += 1

new_positions_round = rock_registry_round

weights = []
previous_maps = []
has_cycled = False
cycle_index = 0

for i in range(0, 1000000000):
    previous_maps.append(new_positions_round.copy())
    new_positions_round = roll(
        new_positions_round, rock_registry_square, LINE, COL, -1, 0)

    new_positions_round = roll(
        new_positions_round, rock_registry_square, LINE, COL, 0, -1)

    new_positions_round = roll(
        new_positions_round, rock_registry_square, LINE, COL, 1, 0)

    new_positions_round = roll(
        new_positions_round, rock_registry_square, LINE, COL, 0, 1)

    weights.append(get_weight(new_positions_round))

    for map in previous_maps:
        if compare_maps(map, new_positions_round) == 1:
            has_cycled = True
            cycle_index = previous_maps.index(map)
            break
    if has_cycled:
        break

cycle_length = len(weights)-cycle_index
result_index = ((1000000000-cycle_index) % cycle_length) + cycle_index-1

print("Result 1 ", get_weight(new_positions_round))
print("Result 2 ", weights[result_index])
