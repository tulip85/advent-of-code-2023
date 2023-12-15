RESULT1 = 0
RESULT2 = 0

horizontal_lines = {}
vertical_lines = {}
LINE_NBR = 0


def find_mirrors_one_dir(input_lines: dict[int, str], error_budget: int = 0) -> int:
    """ Function that finds the position of the mirror with a maximum of x changes (error budget)"""

    for potential_mirror in range(0, len(input_lines)-1):
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

    return -1


def find_mirrors(horizontal: dict[int, str], vertical: dict[int, str], error_budget: int = 0) -> int:
    """ Finds the mirrored line and returns the value depending on whether it's a horizontal or vertical mirror"""
    mirror = find_mirrors_one_dir(horizontal, error_budget)

    if mirror == -1:
        mirror = find_mirrors_one_dir(vertical, error_budget)
        return mirror+1
    else:
        return (mirror+1)*100


for line in open("Day13/input1.in", encoding="utf-8"):
    line = line.strip()
    if line.strip() == "":
        RESULT1 += find_mirrors(horizontal_lines, vertical_lines)
        RESULT2 += find_mirrors(horizontal_lines, vertical_lines, 1)

        LINE_NBR = 0
        COL_NBR = 0
        horizontal_lines = {}
        vertical_lines = {}
    else:
        COL_NBR = 0
        horizontal_lines[LINE_NBR] = line
        for char in line:
            if COL_NBR not in vertical_lines:
                vertical_lines[COL_NBR] = ""
            vertical_lines[COL_NBR] += char
            COL_NBR += 1
        LINE_NBR += 1


RESULT1 += find_mirrors(horizontal_lines, vertical_lines)
RESULT2 += find_mirrors(horizontal_lines, vertical_lines, 1)

print("Result1", RESULT1)
print("Result2", RESULT2)
