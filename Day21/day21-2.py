from functools import cache
from ast import literal_eval

GARDEN_PLOT_REGISTRY = []
ROCK_REGISTRY = []

start = (0, 9)
LINE_IND = 0
for line in open("Day21/input1.in", encoding="utf-8"):
    COL = 0
    for item in line:
        if item == ".":
            GARDEN_PLOT_REGISTRY.append((LINE_IND, COL))
        elif item == "S":
            start = (LINE_IND, COL)
            GARDEN_PLOT_REGISTRY.append((LINE_IND, COL))
        COL += 1
    LINE_IND += 1

# replicate x times:
offset = 131
print("replicating")
for replicas in range(0, 1):
    for item in GARDEN_PLOT_REGISTRY:
        GARDEN_PLOT_REGISTRY.append((item[0]+offset, item[1]))
        GARDEN_PLOT_REGISTRY.append((item[0]-offset, item[1]))
        GARDEN_PLOT_REGISTRY.append((item[0], item[1]+offset))
        GARDEN_PLOT_REGISTRY.append((item[0], item[1]-offset))
    offset += 131

start = (start[0] + offset, start[1]+offset)
print("done replicating")
print(start)
queue = [start]

# MAX_STEPS_1 = 26501365
MAX_STEPS_1 = 65+131


@cache
def get_next_steps(queue_string):
    queue = [(x, y) for (x, y) in literal_eval(queue_string)]
    out_queue = set()

    for (x, y) in queue:

        if x == 65 and y == 0:
            print(STEP)

        if (x-1, y) in GARDEN_PLOT_REGISTRY:
            out_queue.add((x-1, y))
        if (x+1, y) in GARDEN_PLOT_REGISTRY:
            out_queue.add((x+1, y))
        if (x, y-1) in GARDEN_PLOT_REGISTRY:
            out_queue.add((x, y-1))
        if (x, y+1) in GARDEN_PLOT_REGISTRY:
            out_queue.add((x, y+1))

    return out_queue


last_four_len = [0, 0, 0, 0]
STEP = 0

while STEP < MAX_STEPS_1:
    STEP += 1
    queue = get_next_steps(str(queue))

    last_four_len.append((len(queue)))
    last_four_len = last_four_len[1:]
    print(STEP)

    if STEP == 65:
        print("65", len(queue))

    if STEP == 66:
        print("66", len(queue))

    if STEP == 67:
        print("67", len(queue))

    if STEP == 68:
        print("68", len(queue))


print("Result 1", len(queue))
