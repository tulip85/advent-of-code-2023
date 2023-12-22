from functools import cache
from ast import literal_eval

GARDEN_PLOT_REGISTRY = []
ROCK_REGISTRY = []

start = (0, 9)
LINE_IND = 0
for line in open("Day21/input1.in", encoding="utf-8"):
    COL = 0
    for item in line:
        if item == "#":
            ROCK_REGISTRY.append((LINE_IND, COL))
        elif item == ".":
            GARDEN_PLOT_REGISTRY.append((LINE_IND, COL))
        elif item == "S":
            start = (LINE_IND, COL)
            GARDEN_PLOT_REGISTRY.append((LINE_IND, COL))
        COL += 1
    LINE_IND += 1


queue = [start]

MAX_STEPS_1 = 64


@cache
def get_next_steps(queue_string):
    queue = [(x, y) for (x, y) in literal_eval(queue_string)]
    out_queue = set()

    for (x, y) in queue:
        if (x-1, y) in GARDEN_PLOT_REGISTRY:
            out_queue.add((x-1, y))
        if (x+1, y) in GARDEN_PLOT_REGISTRY:
            out_queue.add((x+1, y))
        if (x, y-1) in GARDEN_PLOT_REGISTRY:
            out_queue.add((x, y-1))
        if (x, y+1) in GARDEN_PLOT_REGISTRY:
            out_queue.add((x, y+1))

    return out_queue


for step in range(0, MAX_STEPS_1):
    queue = get_next_steps(str(queue))


print("Result 1", len(queue))
