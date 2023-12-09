from itertools import pairwise

input_file = open("Day9/input1.in", encoding="utf-8")

RESULT_1 = 0
RESULT_2 = 0


def predict_item(sequence, last=True):
    ''' Predicts an item at the beginning (last=False) or end of a list'''
    # if all the same numbers in the list, return that number
    if len(set(sequence)) == 1:
        return sequence[0]

    # otherwise compute a list of differences
    differences = [y-x for (x, y) in pairwise(sequence)]

    # depending on whether looking for the first or last element, do the recursion
    if last:
        return sequence[len(sequence)-1] + predict_item(differences)
    return sequence[0] - predict_item(differences, False)


for line in input_file:
    input_sequence = [int(x) for x in line.split()]
    RESULT_1 += predict_item(input_sequence)
    RESULT_2 += predict_item(input_sequence, False)

print("Result 1: ", RESULT_1)
print("Result 2: ", RESULT_2)
