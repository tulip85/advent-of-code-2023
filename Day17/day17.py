from heapq import heappop, heappush

input_map = {}
visited = set()

LINE = 0

for line in open("Day17/input1.in", encoding="utf-8"):
    COL = 0
    for char in line.strip():
        input_map[(LINE, COL)] = int(char)

        COL += 1
    LINE += 1

TOTAL_COLS = COL - 1
TOTAL_LINES = LINE - 1


def treat_candidate_part_1(x, y, val_up_now, direction, same_dir_count, new_direction, opposite):

    if TOTAL_LINES >= x >= 0 and TOTAL_COLS >= y >= 0 and direction != opposite:
        node_val = input_map[(x, y)]+val_up_now
        if new_direction == direction:
            if same_dir_count < 3:
                heappush(
                    DIJKSTRA, (node_val, x, y, new_direction, same_dir_count+1))

        else:
            heappush(
                DIJKSTRA, (node_val, x, y, new_direction, 1))


def treat_candidate_part_2(x, y, val_up_now, direction, same_dir_count, new_direction, opposite):

    if TOTAL_LINES >= x >= 0 and TOTAL_COLS >= y >= 0 and direction != opposite:
        node_val = input_map[(x, y)]+val_up_now
        if new_direction == direction:
            if same_dir_count < 10:
                heappush(
                    DIJKSTRA, (node_val, x, y, new_direction, same_dir_count+1))

        elif same_dir_count >= 4 or direction == "S":
            heappush(
                DIJKSTRA, (node_val, x, y, new_direction, 1))


DIJKSTRA = []


# accumulated heat, line, column, direction, moved in the same direction
heappush(DIJKSTRA, (0, 0, 0, "S", 0))

# Part 1
while len(DIJKSTRA) > 0:

    curr_node = heappop(DIJKSTRA)
    node_line = curr_node[1]
    node_col = curr_node[2]
    last_dir = curr_node[3]
    count_dir = curr_node[4]
    curr_val = curr_node[0]

    if node_col == TOTAL_COLS and node_line == TOTAL_LINES:
        print("Result 1", curr_val)
        break

    if (node_line, node_col, last_dir, count_dir) not in visited:

        visited.add((node_line, node_col,
                     last_dir, count_dir))

        # find the shortest node away that has not been visited
        treat_candidate_part_1(node_line-1, node_col,
                               curr_val, last_dir, count_dir, "U", "D")
        treat_candidate_part_1(node_line+1, node_col,
                               curr_val, last_dir, count_dir, "D", "U")
        treat_candidate_part_1(node_line, node_col-1,
                               curr_val, last_dir, count_dir, "L", "R")
        treat_candidate_part_1(node_line, node_col+1,
                               curr_val, last_dir, count_dir, "R", "L")


DIJKSTRA = []
# accumulated heat, line, column, direction, moved in the same direction
heappush(DIJKSTRA, (0, 0, 0, "S", 0))

visited = set()

# Part 1
while len(DIJKSTRA) > 0:

    curr_node = heappop(DIJKSTRA)
    node_line = curr_node[1]
    node_col = curr_node[2]
    last_dir = curr_node[3]
    count_dir = curr_node[4]
    curr_val = curr_node[0]

    if node_col == TOTAL_COLS and node_line == TOTAL_LINES:
        print("Result 2", curr_val)
        break

    if (node_line, node_col, last_dir, count_dir) not in visited:

        visited.add((node_line, node_col,
                     last_dir, count_dir))

        # find the shortest node away that has not been visited
        treat_candidate_part_2(node_line-1, node_col,
                               curr_val, last_dir, count_dir, "U", "D")
        treat_candidate_part_2(node_line+1, node_col,
                               curr_val, last_dir, count_dir, "D", "U")
        treat_candidate_part_2(node_line, node_col-1,
                               curr_val, last_dir, count_dir, "L", "R")
        treat_candidate_part_2(node_line, node_col+1,
                               curr_val, last_dir, count_dir, "R", "L")
