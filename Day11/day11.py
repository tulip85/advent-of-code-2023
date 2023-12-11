from itertools import combinations

input_file = open("Day11/input1.in", encoding="utf-8")

LINE_IDX = 0
COL_IDX = 0

EXPANDED_GLX_LINE = []
EXPANDED_GLX_COL = []
GALAXIES = {}


def calculate_distance_two_pairs(pair1, pair2, exp_factor=1):

    start_col = min(pair1[1], pair2[1])
    end_col = max(pair1[1], pair2[1])
    start_line = min(pair1[0], pair2[0])
    end_line = max(pair1[0], pair2[0])

    exp_col = 0
    for i in range(start_col+1, end_col):
        if i in EXPANDED_GLX_COL:
            exp_col += 1

    exp_line = 0
    for i in range(start_line+1, end_line):
        if i in EXPANDED_GLX_LINE:
            exp_line += 1

    return ((end_col+(exp_col*exp_factor))-start_col) + ((end_line+(exp_line*exp_factor))-start_line)


GALAXY_CNT = 1
# Read input and populate data structures
for line in input_file:
    line = line.strip()
    if LINE_IDX == 0:
        for i in range(0, len(line)):
            EXPANDED_GLX_COL.append(i)
    if line.count(".") == len(line):
        EXPANDED_GLX_LINE.append(LINE_IDX)
    else:
        COL_IDX = 0
        for char in line:
            if char == "#":
                GALAXIES[GALAXY_CNT] = ((LINE_IDX, COL_IDX))
                GALAXY_CNT += 1
                if COL_IDX in EXPANDED_GLX_COL:
                    EXPANDED_GLX_COL.remove(COL_IDX)

            COL_IDX += 1

    LINE_IDX += 1

# calculate distances between all pairs
SLICER = int(len(GALAXIES)/2)
RESULT1 = 0
RESULT2 = 0

for (p1, p2) in list(combinations(GALAXIES.keys(), 2)):
    RESULT1 += calculate_distance_two_pairs(GALAXIES[p1], GALAXIES[p2])
    RESULT2 += calculate_distance_two_pairs(
        GALAXIES[p1], GALAXIES[p2], 1000000-1)

print("Result 1: ", RESULT1)
print("Result 2: ", RESULT2)
