from collections import deque


VALID_STEPS_SET = set()
SIMPLIFIED_VALID_STEPS = {}


LINE = 0
for line in open("Day23/input1.in", encoding="utf-8"):
    COL = 0
    for item in line:
        if item in [".", ">", "^", "<", "v"]:
            VALID_STEPS_SET.add((LINE, COL))

        COL += 1
    LINE += 1
TOTAL_LINES = LINE-1
TOTAL_COLS = COL-1

START = (0, 1)
END = (TOTAL_LINES, TOTAL_COLS-1)
MAX_CORRIDOR = 0

SIMPLIFIED_ADJACENCY_WEIGHTS = {}

DISTANCES = {}


def simplify_graph():
    global SIMPLIFIED_VALID_STEPS

    for node in VALID_STEPS_SET:
        neighbours = {}
        if (node[0]-1, node[1]) in VALID_STEPS_SET:
            neighbours[(node[0]-1, node[1])] = 1
        if (node[0]+1, node[1]) in VALID_STEPS_SET:
            neighbours[(node[0]+1, node[1])] = 1
        if (node[0], node[1]-1) in VALID_STEPS_SET:
            neighbours[(node[0], node[1]-1)] = 1
        if (node[0], node[1]+1) in VALID_STEPS_SET:
            neighbours[(node[0], node[1]+1)] = 1

        SIMPLIFIED_VALID_STEPS[node] = neighbours

    # collapse neighbours
    nodes_to_delete = set()
    for node, neighbours in SIMPLIFIED_VALID_STEPS.items():
        if len(neighbours) == 2:
            neighbour_keys = list(neighbours.keys())
            neighbour_1 = neighbour_keys[0]
            neighbour_2 = neighbour_keys[1]
            new_value = SIMPLIFIED_VALID_STEPS[neighbour_1][node] + \
                SIMPLIFIED_VALID_STEPS[neighbour_2][node]
            SIMPLIFIED_VALID_STEPS[neighbour_1][neighbour_2] = new_value
            SIMPLIFIED_VALID_STEPS[neighbour_2][neighbour_1] = new_value
            del SIMPLIFIED_VALID_STEPS[neighbour_1][node]
            del SIMPLIFIED_VALID_STEPS[neighbour_2][node]
            nodes_to_delete.add(node)

    for node in nodes_to_delete:
        del SIMPLIFIED_VALID_STEPS[node]


def treat_candidate_part_1(x, y, new_length, curr_path_in):
    new_path = curr_path_in.copy()
    new_path.add((x, y))
    BFS.append([x, y, new_length, new_path])


BFS = deque([])
VISITED = set()

# path length, line, col, last direction, slope "budget", length, current_path
BFS.append([0, 1, 0, set([(0, 1)])])

RESULTS = set()

LAST_MAX = 0

VALID_STEPS_SET = sorted(VALID_STEPS_SET)


simplify_graph()

print(SIMPLIFIED_VALID_STEPS)

# Part 1
while len(BFS) > 0:

    curr_node = BFS.pop()
    node_line = curr_node[0]
    node_col = curr_node[1]
    curr_length = curr_node[2]
    curr_path = curr_node[3]

    if node_col == END[1] and node_line == END[0]:

        if curr_length > LAST_MAX:
            LAST_MAX = curr_length
            RESULTS.add(curr_length)
            print("Updated maximum ", curr_length)

    # find the shortest node away that has not been visited
    for neighbour in SIMPLIFIED_VALID_STEPS[(node_line, node_col)]:
        corridor_length = SIMPLIFIED_VALID_STEPS[(
            node_line, node_col)][neighbour]

        if neighbour not in curr_path:
            treat_candidate_part_1(neighbour[0], neighbour[1], curr_length+corridor_length,
                                   curr_path)

print("Result 1", LAST_MAX)
