input_file = open("Day2/input1.in", encoding="utf-8")

total_cubes = {"red": 12, "green": 13, "blue": 14}

RESULT_1 = 0
RESULT_2 = 0

for line in input_file:
    POSSIBLE = True
    min_cubes = {"red": 0, "green": 0, "blue": 0}

    game_set = line.split(":")
    sets = game_set[1].split(";")
    game = int(game_set[0].split(" ")[1])

    for set_in in sets:
        cubes_drawn = set_in.split(",")
        for cubes in cubes_drawn:
            tuple_in = cubes.strip().split(" ")
            if total_cubes[tuple_in[1]] < int(tuple_in[0]):
                POSSIBLE = False
            if min_cubes[tuple_in[1]] < int(tuple_in[0]):
                min_cubes[tuple_in[1]] = int(tuple_in[0])

    if POSSIBLE:
        RESULT_1 = RESULT_1+game

    # calculate power
    RESULT_2 = RESULT_2 + \
        (min_cubes["red"]*min_cubes["blue"]*min_cubes["green"])

print("Result 1", RESULT_1)
print("Result 2", RESULT_2)
