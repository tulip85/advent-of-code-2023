import ast
import copy

WFL = {}
PARTS = []

READING_INSTR = True
for line in open("Day19/input1.in", encoding="utf-8"):
    if line.strip() != "" and READING_INSTR:
        WFL[line.split("{")[0]] = line.strip().split(
            "{")[1].replace("}", "").split(",")
    elif line.strip() == "":
        READING_INSTR = False
    else:
        input_items = line.strip().replace(
            "{", "").replace("}", "").split(",")
        DICT_IN = {}
        for in_item in input_items:
            DICT_IN[in_item.split("=")[0]] = in_item.split("=")[1]
        PARTS.append(DICT_IN)

REJECTED = []
ACCEPTED = []


def record_decision(decision_in, target, part):
    if decision_in == "A" or target == "A":
        CURR_WFL = "A"
        IS_DONE = True
        ACCEPTED.append(part)
    elif decision_in == "R" or target == "R":
        CURR_WFL = "R"
        IS_DONE = True
        REJECTED.append(part)
    else:
        CURR_WFL = target
        IS_DONE = False

    return (CURR_WFL, IS_DONE)


for part in PARTS:
    CURR_WFL = "in"
    IS_DONE = False

    x = int(part["x"])
    m = int(part["m"])
    a = int(part["a"])
    s = int(part["s"])

    while not IS_DONE:
        instr = WFL[CURR_WFL]
        for decision in instr:

            if ":" not in decision:
                target = decision.split(":")[0]
                CURR_WFL, IS_DONE = record_decision(decision, target, part)
            else:
                eval_statement = decision.split(":")[0]
                target = decision.split(":")[1]
                if eval(eval_statement):
                    CURR_WFL, IS_DONE = record_decision(decision, target, part)
                    break

RESULT1 = 0
for acc_part in ACCEPTED:
    for var in acc_part:
        RESULT1 += int(acc_part[var])

print("Result 1", RESULT1)


WINNING_RANGES = []


def treat_workflow(workflow_name, workflow_step, ranges_in):
    ranges = copy.deepcopy(ranges_in)

    if workflow_name == "A" or (workflow_name != "R" and WFL[workflow_name][workflow_step] == "A"):
        return (ranges["x"][1]+1-ranges["x"][0])*(ranges["m"][1]+1-ranges["m"][0])*(ranges["a"][1]+1-ranges["a"][0])*(ranges["s"][1]+1-ranges["s"][0])
    if workflow_name == "R" or WFL[workflow_name][workflow_step] == "R":
        return 0

    curr_workflow = WFL[workflow_name][workflow_step]

    if ":" not in curr_workflow:
        return treat_workflow(curr_workflow, 0, ranges)
    else:

        target_wfl = curr_workflow.split(":")[1]
        eval_string = curr_workflow.split(":")[0]
        operator = "<" if "<" in eval_string else ">"
        var_name = eval_string.split(operator)[0]
        value = int(eval_string.split(operator)[1])

        if value < ranges[var_name][1] and value > ranges[var_name][0]:
            wrong_range = copy.deepcopy(ranges)
            right_range = copy.deepcopy(ranges)

            if operator == ">":
                right_range[var_name][0] = value+1
                wrong_range[var_name][1] = value
                return treat_workflow(workflow_name, workflow_step+1, wrong_range) + treat_workflow(target_wfl, 0, right_range)

            if operator == "<":
                wrong_range[var_name][0] = value
                right_range[var_name][1] = value-1
                return treat_workflow(workflow_name, workflow_step+1, wrong_range) + treat_workflow(target_wfl, 0, right_range)

        if value >= ranges[var_name][1]:
            if operator == ">":
                return treat_workflow(workflow_name, workflow_step+1, ranges)
            else:
                return treat_workflow(target_wfl, 0, ranges)

        if value <= ranges[var_name][0]:
            if operator == "<":
                return treat_workflow(workflow_name, workflow_step+1, ranges)
            else:
                return treat_workflow(target_wfl, 0, ranges)


range_resp = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
workflow = "in"

RESULT2 = treat_workflow(workflow, 0, range_resp)

print("Result 2", RESULT2)
