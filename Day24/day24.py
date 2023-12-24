
LINES = []

test_area_x = [200000000000000, 400000000000000]
test_area_y = [200000000000000, 400000000000000]

# test_area_x = [7, 27]
# test_area_y = [7, 27]

for line in open("Day24/input1.in", encoding="utf-8"):
    parts = line.strip().split("@")
    coordinates = parts[0].strip().split(",")
    speeds = parts[1].strip().split(",")

    coordinates = [int(x) for x in coordinates]
    speeds = [int(x) for x in speeds]

    # add the lines with two coordinates
    LINES.append(((coordinates[0], coordinates[1]),
                 (coordinates[0]+speeds[0]*100, coordinates[1]+speeds[1]*100)))


# formula: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
def find_intersection(line1, line2):
    x1 = line1[0][0]
    x2 = line1[1][0]
    x3 = line2[0][0]
    x4 = line2[1][0]
    y1 = line1[0][1]
    y2 = line1[1][1]
    y3 = line2[0][1]
    y4 = line2[1][1]

    try:
        px = ((x1*y2 - y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4)) / \
            ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        py = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4)) / \
            ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        return (px, py)
    except ZeroDivisionError:
        # When the two lines are parallel or coincident, the denominator is zero.
        return -1


def is_in_past(line, point):

    if (point[0] > line[0][0]) == (line[1][0] > line[0][0]):
        if (point[1] > line[0][1]) == (line[1][1] > line[0][1]):
            return False

    return True


COMBINATIONS = {}

Result1 = 0

for line1 in LINES:
    for line2 in LINES:
        if (line1, line2) not in COMBINATIONS and (line2, line1) not in COMBINATIONS and line2 != line1:
            intersection = find_intersection(line1, line2)
            COMBINATIONS[(line1, line2)] = intersection
            if intersection != -1:
                if intersection[0] >= test_area_x[0] and intersection[0] <= test_area_x[1] and intersection[1] >= test_area_y[0] and intersection[1] <= test_area_y[1]:
                    # test if the crossing is in the past
                    if not is_in_past(line1, intersection) and not is_in_past(line2, intersection):
                        Result1 += 1


print("Result 1 ", Result1)

# 18184
