import ast

# Note: very very slow, runs in ~3-7 minutes for part 2

instr = []

LINE = 0

for line in open("Day18/input1.in", encoding="utf-8"):
    instr.append(line.split())

GRID = {}


DISTANCE_MAPPER = {0: "R", 1: "D", 2: "L", 3: "U"}


def get_area_with_shoelace(coordinates):
    coordinates = list(coordinates)
    total_length = len(coordinates)
    shoelace_area = abs(sum(
        (v1[0] + v2[0])*(v1[1] - v2[1]) / 2
        for v1, v2 in zip(coordinates, coordinates[1:])
    ))
    return int(shoelace_area + total_length/2 + 1)


def get_distance_hex(instruction):
    instr = instruction.replace("(", "").replace(")", "").replace("#", "0x")
    distance = ast.literal_eval(instr[0:7])
    return distance


def get_direction_hex(instruction):
    instr = instruction.replace("(", "").replace(")", "").replace("#", "")
    return DISTANCE_MAPPER[int(instr[-1])]


def mark_and_get_new_pos(pos, direction, count):

    new_pos = (0, 0)
    match direction:
        case "U":
            for i in range(pos[0], pos[0]-count-1, -1):
                GRID[(i, pos[1])] = "#"
            new_pos = (pos[0]-count, pos[1])
        case "D":
            for i in range(pos[0], pos[0]+count+1):
                GRID[(i, pos[1])] = "#"
            new_pos = (pos[0]+count, pos[1])
        case "L":
            for i in range(pos[1], pos[1]-count-1, -1):
                GRID[(pos[0], i)] = "#"
            new_pos = (pos[0], pos[1]-count)
        case "R":
            for i in range(pos[1], pos[1]+count+1):
                GRID[(pos[0], i)] = "#"
            new_pos = (pos[0], pos[1]+count)

    return new_pos


def do_part_1(instructions):
    curr_pos = (0, 0)
    # draw the borders
    for instr_set in instructions:
        curr_pos = mark_and_get_new_pos(
            curr_pos, instr_set[0], int(instr_set[1]))

    print("Result 1", get_area_with_shoelace(GRID.keys()))


def do_part_2(instructions):
    curr_pos = (0, 0)
    # draw the borders
    for instr_set in instructions:
        curr_pos = mark_and_get_new_pos(
            curr_pos, get_direction_hex(instr_set[2]), get_distance_hex(instr_set[2]))

    print("Result 2", get_area_with_shoelace(GRID.keys()))


do_part_1(instr)

GRID = {}
do_part_2(instr)
