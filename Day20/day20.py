from enum import Enum
import re
from math import lcm

MODULE_TYPE_REGISTRY = {}
MODULE_DEST_MAPPING = {}
CONJUNCTION_INPUTS = {}
CYCLE_TRACKER = {}
CYLCE_LENGTHS = {}

BROADCASTER = "broadcaster"
global LOW_PULSES_1, HIGH_PULSES_1
LOW_PULSES_1 = 0
HIGH_PULSES_1 = 0
RX_PRESSES_LOW = 0
RX_PRESSES_HIGH = 0

for line in open("Day20/input1.in", encoding="utf-8"):
    line_array = line.strip().split(" -> ")
    source = line_array[0]
    destinations = line_array[1].split(", ")
    if source != BROADCASTER:
        module_type = source[0]
        module_name = source[1:]
    else:
        module_name = BROADCASTER
        module_type = BROADCASTER
    
    MODULE_TYPE_REGISTRY[module_name] = module_type
    MODULE_DEST_MAPPING[module_name] = destinations
    
    if module_type == "&":
        CONJUNCTION_INPUTS[module_name] = {}
    if module_type == "%":
        CYCLE_TRACKER[module_name] = []

#find all the mappings to the conjunction modules
for source, destinations in MODULE_DEST_MAPPING.items():
    for dest in destinations:
        if dest in CONJUNCTION_INPUTS.keys():
            CONJUNCTION_INPUTS[dest][source] = 0
            
def flip_state(state)->int:
    if state == 1:
        return 0
    else:
        return 1

def are_all_high(module_name):
    ALL_HIGH = True
    for input_src in CONJUNCTION_INPUTS[module_name]: 
        if CONJUNCTION_INPUTS[module_name][input_src] == 0:
            ALL_HIGH = False
            
    return ALL_HIGH

def cycle(list):
    shortest = [] 
    if len(list) <= 1: return list
    if len(set(list)) == len(list): return list
    for x in range(len(list)):
        if list[0:x] == list[x:2*x]:
            shortest = list[0:x] 
    return shortest 


def execute_button_press(module_state):
    execution_queue = [(BROADCASTER, 0)]
    
    while len(execution_queue) > 0:

        curr_action = execution_queue.pop(0)
        module_name = curr_action[0]
        curr_pulse = curr_action[1]
        
        global HIGH_PULSES_1, LOW_PULSES_1, RX_PRESSES_LOW

        if curr_pulse == 1:
            HIGH_PULSES_1 += 1
        else:
            LOW_PULSES_1 += 1
        
        if module_name == "rx" and curr_pulse == 0:
            RX_PRESSES_LOW += 1
        
        if module_name in MODULE_TYPE_REGISTRY:
            
            if MODULE_TYPE_REGISTRY[module_name] == BROADCASTER:
                for dest in MODULE_DEST_MAPPING[module_name]:   
                    execution_queue.append((dest, curr_pulse))    
                    if dest in CONJUNCTION_INPUTS.keys(): CONJUNCTION_INPUTS[dest][module_name] = curr_pulse 
                    
            #Flip-flop modules (prefix %) are either on or off; they are initially off. 
            # If a flip-flop module receives a high pulse, it is ignored and nothing happens. 
            # However, if a flip-flop module receives a low pulse, it flips between on and off. 
            # If it was off, it turns on and sends a high pulse. 
            # If it was on, it turns off and sends a low pulse. 
            elif MODULE_TYPE_REGISTRY[module_name] == "%":
                if curr_pulse == 0:
                    new_state = flip_state(module_state[module_name][0])
                    module_state[module_name][0] = new_state
                    for dest in MODULE_DEST_MAPPING[module_name]:   
                        execution_queue.append((dest, new_state))
                        if dest in CONJUNCTION_INPUTS.keys(): 
                            CONJUNCTION_INPUTS[dest][module_name] = new_state 
                        
            # Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected input modules; 
            # they initially default to remembering a low pulse for each input. 
            # When a pulse is received, the conjunction module first updates its memory for that input. 
            # Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.
            elif MODULE_TYPE_REGISTRY[module_name] == "&":
                pulse = not are_all_high(module_name)         

                for dest in MODULE_DEST_MAPPING[module_name]: 
                    execution_queue.append((dest, pulse))
                    if dest in CONJUNCTION_INPUTS.keys(): CONJUNCTION_INPUTS[dest][module_name] = pulse 
            
        
    return module_state
    
all_states = {}

for mod in MODULE_TYPE_REGISTRY:
    all_states[mod] = [0,0]

for button_press in range(0, 10000):
    RX_PRESSES = 0
    all_states = execute_button_press(all_states)
    
    if button_press == 999:
        print("Result1", HIGH_PULSES_1*LOW_PULSES_1, HIGH_PULSES_1, LOW_PULSES_1)
    
    if RX_PRESSES_LOW == 1:
        print("Result2", button_press)
        break
    
    for module in CYCLE_TRACKER:
        CYCLE_TRACKER[module].append(all_states[module][0])


for module in CYCLE_TRACKER:
    CYLCE_LENGTHS[module] = len(cycle(CYCLE_TRACKER[module]))
    
#did a manual drawing of the chart to see the "layers"
gp = [CYLCE_LENGTHS["rj"], CYLCE_LENGTHS["rc"], CYLCE_LENGTHS["ps"], CYLCE_LENGTHS["nd"], CYLCE_LENGTHS["tv"], CYLCE_LENGTHS["rq"]]
bn = [CYLCE_LENGTHS["fs"], CYLCE_LENGTHS["xz"], CYLCE_LENGTHS["gs"], CYLCE_LENGTHS["ft"], CYLCE_LENGTHS["lf"], CYLCE_LENGTHS["vx"]]
rt = [CYLCE_LENGTHS["pn"], CYLCE_LENGTHS["nm"], CYLCE_LENGTHS["dg"], CYLCE_LENGTHS["pp"], CYLCE_LENGTHS["cq"], CYLCE_LENGTHS["bs"], CYLCE_LENGTHS["gn"], CYLCE_LENGTHS["lh"]]
cz = [CYLCE_LENGTHS["mj"], CYLCE_LENGTHS["qd"], CYLCE_LENGTHS["ls"], CYLCE_LENGTHS["sl"], CYLCE_LENGTHS["sh"], CYLCE_LENGTHS["fz"], CYLCE_LENGTHS["vr"], CYLCE_LENGTHS["sz"], CYLCE_LENGTHS["dn"]]

second_layer = [lcm(*gp), lcm(*bn), lcm(*rt), lcm(*cz)]
third_layer = lcm(*second_layer)
print("Result 2", third_layer)