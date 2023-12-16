

TOTAL_COLS = 0
TOTAL_LINES = 0

input_map = {}

LINE = 0
COL = 0


def print_visited(path):

    for i in range(0, TOTAL_LINES+1):
        line = ""
        for j in range(0, TOTAL_COLS+1):
            if (i, j) in path:
                line += "#"
            else:
                line += "."

        print(line)


def get_next_position(point, direction):
    # only return the items that are not out

    current_point = input_map[point]
    return_map = []

    if current_point == ".":
        match direction:
            case "U":
                return_map.append((point[0]-1, point[1], direction))
            case "D":
                return_map.append((point[0]+1, point[1], direction))
            case "L":
                return_map.append((point[0], point[1]-1, direction))
            case "R":
                return_map.append((point[0], point[1]+1, direction))
    elif current_point == "/":
        match direction:
            case "U":
                return_map.append((point[0], point[1]+1, "R"))
            case "D":
                return_map.append((point[0], point[1]-1, "L"))
            case "L":
                return_map.append((point[0]+1, point[1], "D"))
            case "R":
                return_map.append((point[0]-1, point[1], "U"))
    elif current_point == "L":
        match direction:
            case "D":
                return_map.append((point[0], point[1]+1, "R"))
            case "U":
                return_map.append((point[0], point[1]-1, "L"))
            case "R":
                return_map.append((point[0]+1, point[1], "D"))
            case "L":
                return_map.append((point[0]-1, point[1], "U"))
    elif current_point == "-":
        match direction:
            case "D":
                return_map.append((point[0], point[1]+1, "R"))
                return_map.append((point[0], point[1]-1, "L"))
            case "U":
                return_map.append((point[0], point[1]+1, "R"))
                return_map.append((point[0], point[1]-1, "L"))
            case "R":
                return_map.append((point[0], point[1]+1, direction))
            case "L":
                return_map.append((point[0], point[1]-1, direction))
    elif current_point == "|":
        match direction:
            case "D":
                return_map.append((point[0]+1, point[1], direction))
            case "U":
                return_map.append((point[0]-1, point[1], direction))
            case "R":
                return_map.append((point[0]-1, point[1], "U"))
                return_map.append((point[0]+1, point[1], "D"))
            case "L":
                return_map.append((point[0]-1, point[1], "U"))
                return_map.append((point[0]+1, point[1], "D"))

    # remove targets that are outside the grid
    return_only_in = []
    for item in return_map:
        if not is_out(item):
            return_only_in.append(item)

    return return_only_in


def is_looping(triple) -> bool:

    if triple in NODES_VISITED:
        return True
    else:
        return False


def is_out(point) -> bool:
    if point[0] > TOTAL_LINES or point[1] > TOTAL_COLS or point[0] < 0 or point[1] < 0:
        return True
    else:
        return False


def get_beam_path(start_point, direction, beam_path) -> list:
    beam_path.append(start_point)

    while True:
        next_lst = get_next_position(start_point, direction)
        if len(next_lst) == 0 or (len(next_lst) == 1 and is_looping(next_lst[0])):
            return beam_path
        elif len(next_lst) == 1:
            beam_path.append((next_lst[0][0], next_lst[0][1]))
            NODES_VISITED.add(next_lst[0])
            direction = next_lst[0][2]
            start_point = (next_lst[0][0], next_lst[0][1])
        elif len(next_lst) == 2:
            first_item = next_lst[0]
            second_item = next_lst[1]
            if is_looping(first_item) and not is_looping(second_item):
                beam_path.append((second_item[0], second_item[1]))
                NODES_VISITED.add(second_item)
                direction = second_item[2]
                start_point = (second_item[0], second_item[1])
            elif is_looping(second_item) and not is_looping(first_item):
                beam_path.append((first_item[0], first_item[1]))
                direction = first_item[2]
                NODES_VISITED.add(first_item)
                start_point = (first_item[0], first_item[1])
            else:
                return get_beam_path((first_item[0], first_item[1]), first_item[2], beam_path.copy()) + get_beam_path((second_item[0], second_item[1]), second_item[2], beam_path.copy())


for line in open("Day16/input1.in", encoding="utf-8"):
    COL = 0
    line = line.replace("\\", "L")
    for char in line.strip():
        input_map[(LINE, COL)] = char
        COL += 1
    LINE += 1


TOTAL_COLS = COL - 1
TOTAL_LINES = LINE - 1

NODES_VISITED = set((0, 0, "R"))

path = get_beam_path((0, 0), "R", [])

print("Result 1", len(set(path)))

RESULT2 = 0

for i in range(0, TOTAL_COLS):
    NODES_VISITED = set((0, i, "D"))
    LEN_PATH = len(set(get_beam_path((0, i), "D", [])))
    if LEN_PATH > RESULT2:
        RESULT2 = LEN_PATH

    NODES_VISITED = set((TOTAL_LINES, i, "U"))
    LEN_PATH = len(set(get_beam_path((TOTAL_LINES, i), "U", [])))
    if LEN_PATH > RESULT2:
        RESULT2 = LEN_PATH

for i in range(0, TOTAL_LINES):
    NODES_VISITED = set((i, 0, "R"))
    LEN_PATH = len(set(get_beam_path((i, 0), "R", [])))
    if LEN_PATH > RESULT2:
        RESULT2 = LEN_PATH

    NODES_VISITED = set((i, TOTAL_COLS, "L"))
    LEN_PATH = len(set(get_beam_path((i, TOTAL_COLS), "L", [])))
    if LEN_PATH > RESULT2:
        RESULT2 = LEN_PATH

print("Result 2", RESULT2)
