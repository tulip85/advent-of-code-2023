input_file = open("Day10/input1.in", encoding="utf-8")

graph_input = {}
start_index = (0, 0)

get_node_targets = {"|": ["N", "S"], "-": ["E", "W"],
                    "L": ["N", "E"], "J": ["N", "W"], "7": ["S", "W"],
                    "F": ["S", "E"], ".": [], "S": ["N", "W"]}

LINE_INDEX = 0
for line in input_file:
    COL_INDEX = 0
    for item in line.strip():
        graph_input[(LINE_INDEX, COL_INDEX)] = item
        if item == 'S':
            start_index = (LINE_INDEX, COL_INDEX)
        COL_INDEX += 1
    LINE_INDEX += 1

blown_up_grid = {}

LOOP_FOUND = False

node_list = [[(start_index[0], start_index[1])]]
loop_sequence = []

while True:
    next_layer = []
    for sequence in node_list:
        node = sequence[len(sequence)-1]
        targets = get_node_targets[graph_input[node]]
        for target in targets:
            NEXT_NODE = None
            match target:
                case "N":
                    if node[0] > 0:
                        NEXT_NODE = (node[0]-1, node[1])
                case "S":
                    if node[0] < LINE_INDEX:
                        NEXT_NODE = (node[0]+1, node[1])
                case "W":
                    if node[1] > 0:
                        NEXT_NODE = (node[0], node[1]-1)
                case "E":
                    if node[1] < COL_INDEX:
                        NEXT_NODE = (node[0], node[1]+1)

            if (NEXT_NODE is not None and NEXT_NODE not in sequence):
                new_seq = sequence.copy()
                new_seq.append(NEXT_NODE)
                next_layer.append(new_seq)
            elif NEXT_NODE == start_index and NEXT_NODE != sequence[len(sequence)-2]:
                print("Result 1", len(sequence)/2)
                loop_sequence = sequence
                LOOP_FOUND = True
                break
        if LOOP_FOUND:
            break

    if not LOOP_FOUND:
        node_list = next_layer
    else:
        break

visited_nodes = [(0, 0)]

dfs = [(0, 0)]

COUNT = 0
CURR_IN = False
for line in range(0, LINE_INDEX):
    NORTH = 0
    SOUTH = 0
    for col in range(0, COL_INDEX-1):
        if (line, col) in loop_sequence:
            if "N" in get_node_targets[graph_input[(line, col)]]:
                NORTH += 1
            if "S" in get_node_targets[graph_input[(line, col)]]:
                SOUTH += 1
            if SOUTH % 2 != 0 and NORTH % 2 != 0:
                CURR_IN = True
            else:
                CURR_IN = False
        elif CURR_IN:
            COUNT += 1

print("Result 2", COUNT)
