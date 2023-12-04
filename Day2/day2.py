input = open("Day2/input1.in")

total_cubes = {"red": 12, "green": 13, "blue": 14}

result_1 = 0
result_2 = 0

for line in input:
    possible = True
    min_cubes = {"red": 0, "green": 0, "blue": 0}

    game_set = line.split(":")
    sets = game_set[1].split(";")
    game = int(game_set[0].split(" ")[1])

    for set in sets:
        cubes_drawn = set.split(",")
        for cubes in cubes_drawn:
            tuple = cubes.strip().split(" ")
            if total_cubes[tuple[1]] < int(tuple[0]):
                possible = False
            if min_cubes[tuple[1]] < int(tuple[0]):
                min_cubes[tuple[1]] = int(tuple[0])

    if possible:
        result_1 = result_1+game

    # calculate power
    result_2 = result_2 + \
        (min_cubes["red"]*min_cubes["blue"]*min_cubes["green"])

print(result_1)
print(result_2)
