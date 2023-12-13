from copy import deepcopy
RESULT1 = 0
RESULT2 = 0

input_file = open("Day13/input1.in", encoding="utf-8")

horizontal_lines = {}
vertical_lines = {}
LINE_NBR = 0


def find_mirrors_one_dir(input_lines_in, error_budget=0):
    input_lines = input_lines_in.copy()
    candidate_mirrors = [x for x in range(0, len(input_lines)-1)]

    for line in input_lines:
        input_lines[line] = "".join(input_lines[line].values())

    while True:
        if len(candidate_mirrors) == 0:
            return -1
        potential_mirror = candidate_mirrors.pop()
        number_lines_to_consider = min(
            len(input_lines)-potential_mirror-1, potential_mirror+1)
        is_mirrored = True
        mirror_error_budget = error_budget
        for i in range(0, number_lines_to_consider):
            differences = sum(1 for a, b in zip(
                input_lines[potential_mirror-i], input_lines[potential_mirror+i+1]) if a != b)

            if differences > error_budget:
                is_mirrored = False
                break

            if differences > 0:
                mirror_error_budget -= 1
        if is_mirrored and mirror_error_budget == 0:
            return potential_mirror


def find_mirrors(horizontal, vertical):
    mirror = find_mirrors_one_dir(horizontal)

    if mirror == -1:
        mirror = find_mirrors_one_dir(vertical)
        return mirror+1
    else:
        return (mirror+1)*100


def find_mirrors_with_smudge(horizontal, vertical):
    mirror = find_mirrors_one_dir(horizontal, 1)

    if mirror == -1:
        mirror = find_mirrors_one_dir(vertical, 1)
        return mirror+1
    else:
        return (mirror+1)*100


for line in input_file:
    line = line.strip()
    if line.strip() == "":
        RESULT1 += find_mirrors(horizontal_lines, vertical_lines)
        RESULT2 += find_mirrors_with_smudge(horizontal_lines, vertical_lines)
        LINE_NBR = 0
        COL_NBR = 0
        horizontal_lines = {}
        vertical_lines = {}
    else:
        COL_NBR = 0
        horizontal_lines[LINE_NBR] = {}
        for char in line:
            horizontal_lines[LINE_NBR][COL_NBR] = char
            if COL_NBR not in vertical_lines:
                vertical_lines[COL_NBR] = {}
            vertical_lines[COL_NBR][LINE_NBR] = char
            COL_NBR += 1
        LINE_NBR += 1


RESULT1 += find_mirrors(horizontal_lines, vertical_lines)
RESULT2 += find_mirrors_with_smudge(horizontal_lines, vertical_lines)

print("Result1", RESULT1)
print("Result2", RESULT2)
