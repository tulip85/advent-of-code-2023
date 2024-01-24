
from copy import deepcopy
WIRED_CONNECTIONS = {}
WIRES = []

for line in open("Day25/input1.in", encoding="utf-8"):
    parts = line.strip().split(":")
    start = parts[0].strip()
    ends = parts[1].strip().split(" ")

    for end in ends:
        if end not in WIRED_CONNECTIONS:
            WIRED_CONNECTIONS[end] = []
        if start not in WIRED_CONNECTIONS:
            WIRED_CONNECTIONS[start] = []

        WIRED_CONNECTIONS[end].append(start)
        WIRED_CONNECTIONS[start].append(end)
        WIRES.append((start, end))
        WIRES.append((end, start))


print(WIRED_CONNECTIONS)
for wire1 in WIRES:
    for wire2 in WIRES:
        for wire3 in WIRES:
            SIMULATION = deepcopy(WIRED_CONNECTIONS)
            if wire1[0] in SIMULATION[wire1[1]]:
                SIMULATION[wire1[0]].remove(wire1[1])
                SIMULATION[wire1[1]].remove(wire1[0])
            if wire2[0] in SIMULATION[wire2[1]]:
                SIMULATION[wire2[0]].remove(wire2[1])
                SIMULATION[wire2[1]].remove(wire2[0])
            if wire3[0] in SIMULATION[wire3[1]]:
                SIMULATION[wire3[0]].remove(wire3[1])
                SIMULATION[wire3[1]].remove(wire3[0])
            for line in SIMULATION:
                print(SIMULATION)
