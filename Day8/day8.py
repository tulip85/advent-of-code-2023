from math import lcm

input_file = open("Day8/input1.in", encoding="utf-8")

instructions = input_file.readline().strip()

node_mapping_left = {}
node_mapping_right = {}
start_nodes = []

for node_mapping_line in input_file:
    source = node_mapping_line.split("=")[0].strip()
    node_mapping_left[source] = node_mapping_line.split("=")[1].strip().split(
        ",")[0].strip().replace('(', '')
    node_mapping_right[source] = node_mapping_line.split("=")[1].strip().split(",")[
        1].strip().replace(')', '')
    if source[2] == 'A':
        start_nodes.append(source)

''' Part 1 '''

CURR_NODE = 'AAA'
STEPS = 0

while CURR_NODE != 'ZZZ':
    STEPS += 1
    if instructions[STEPS % len(instructions)-1] == 'L':
        CURR_NODE = node_mapping_left[CURR_NODE]
    else:
        CURR_NODE = node_mapping_right[CURR_NODE]

print("Result1", STEPS)

''' Part 2 (only works in this way because the input set has been specially crafted)'''

cycles_to_z = []

for node in start_nodes:
    CYCLE = 1
    while node[2] != 'Z':
        instr = instructions[CYCLE % len(instructions)-1]
        if instr == 'L':
            node = node_mapping_left[node]
        else:
            node = node_mapping_right[node]
        CYCLE += 1
    cycles_to_z.append(CYCLE-1)

print("Result2", lcm(*cycles_to_z))
