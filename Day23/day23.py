from heapq import heappush, heappop

PATH_REGISTRY = []
FOREST_REGISTRY = []
SLOPE_UP = []
SLOPE_RIGHT = []
SLOPE_DOWN = []
SLOPE_LEFT = []
VALID_STEPS = {}


LINE = 0
for line in open("Day23/input1.in", encoding="utf-8"):
    COL = 0
    for item in line:
        if item == ".":
            PATH_REGISTRY.append((LINE, COL))
            VALID_STEPS[(LINE, COL)] = "."
        elif item == "#":
            FOREST_REGISTRY.append((LINE, COL))
        elif item == ">":
            SLOPE_RIGHT.append((LINE, COL))
            VALID_STEPS[(LINE, COL)] = ">"
        elif item == "^":
            SLOPE_UP.append((LINE, COL))
            VALID_STEPS[(LINE, COL)] = "^"
        elif item == "<":
            SLOPE_LEFT.append((LINE, COL))
            VALID_STEPS[(LINE, COL)] = "<"
        elif item == "v":
            SLOPE_DOWN.append((LINE, COL))
            VALID_STEPS[(LINE, COL)] = "v"
        COL += 1
    LINE += 1
TOTAL_LINES = LINE-1
TOTAL_COLS = COL-1

START = (0, 1)
END = (TOTAL_LINES, TOTAL_COLS-1)


def treat_candidate_part_1(x, y, slope_budget_in, path_length, new_direction, curr_path):
    if (x, y) in VALID_STEPS and (x, y) not in curr_path:
        node_type = VALID_STEPS[(x, y)]
        new_slope_budget = "" if node_type == "." else node_type
        if slope_budget_in == "" or (slope_budget_in == ">" and new_direction == "R") or (slope_budget_in == "v" and new_direction == "D") or (slope_budget_in == "^" and new_direction == "U") or (slope_budget_in == "<" and new_direction == "L"):
            new_path = curr_path.copy()
            new_path.append((x, y))
            BFS.append([path_length+1, x, y,
                       new_direction, new_slope_budget, new_path])


BFS = []
VISITED = set()

# path length, line, col, last direction, slope "budget", current_path
BFS.append([0, 0, 1, "S", "", [(0, 1)]])

PATH_LENGTHS = []

# Part 1
while len(BFS) > 0:

    curr_node = BFS.pop()
    node_line = curr_node[1]
    node_col = curr_node[2]
    last_dir = curr_node[3]
    slope_budget = curr_node[4]
    curr_length = curr_node[0]
    curr_path = curr_node[5]

    if node_col == END[1] and node_line == END[0]:
        PATH_LENGTHS.append(curr_length)
    elif (node_line, node_col) not in VISITED:

        # VISITED.add((node_line, node_col))

        # find the shortest node away that has not been visited
        treat_candidate_part_1(node_line-1, node_col,
                               slope_budget, curr_length, "U", curr_path)
        treat_candidate_part_1(node_line+1, node_col,
                               slope_budget, curr_length,  "D", curr_path)
        treat_candidate_part_1(node_line, node_col-1,
                               slope_budget, curr_length, "L", curr_path)
        treat_candidate_part_1(node_line, node_col+1,
                               slope_budget, curr_length, "R", curr_path)

print("Result 1", max(PATH_LENGTHS))
