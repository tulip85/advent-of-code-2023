
from copy import deepcopy
import random
WIRED_CONNECTIONS = {}
WIRES = []

cuts = []
CONTRACTED_NODES = {}
GRAPH = {}


def karger_min_cut():
    global GRAPH
    global CONTRACTED_NODES

    CONTRACTED_NODES = {}

    GRAPH = deepcopy(WIRED_CONNECTIONS)
    while len(GRAPH) > 2:
        first_node = random.choice(list(GRAPH.keys()))
        second_node = random.choice(GRAPH[first_node])
        contract(first_node, second_node)

        if first_node not in CONTRACTED_NODES:
            CONTRACTED_NODES[first_node] = set()
        if second_node not in CONTRACTED_NODES:
            CONTRACTED_NODES[second_node] = set()

        CONTRACTED_NODES[first_node].add(second_node)
        # print(CONTRACTED_NODES)

    mincut = len(GRAPH[list(GRAPH.keys())[0]])
    cuts.append(mincut)

    return mincut


def contract(first_node, second_node):
    for node in GRAPH[second_node]:
        if node != first_node:
            GRAPH[first_node].append(node)
        GRAPH[node].remove(second_node)
        if node != first_node:
            GRAPH[node].append(first_node)

    del GRAPH[second_node]


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


min_cut = 0
while min_cut != 3:
    min_cut = karger_min_cut()


groups = {list(GRAPH.keys())[0]: set(), list(GRAPH.keys())[1]: set()}

stack_1 = [list(GRAPH.keys())[0]]
stack_2 = [list(GRAPH.keys())[1]]

group_size_1 = 0
while len(stack_1) > 0:
    node = stack_1.pop()
    group_size_1 += 1
    if len(CONTRACTED_NODES[node]) > 0:
        for item in CONTRACTED_NODES[node]:
            stack_1.append(item)

group_size_2 = 0
while len(stack_2) > 0:
    node = stack_2.pop()
    group_size_2 += 1
    if len(CONTRACTED_NODES[node]) > 0:
        for item in CONTRACTED_NODES[node]:
            stack_2.append(item)

print(group_size_1, group_size_2, group_size_2*group_size_1)
