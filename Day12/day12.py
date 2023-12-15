from functools import cache
from ast import literal_eval

RESULT1 = 0
RESULT2 = 0


@cache
def find_number_permutations(input_chars, previous_char, check_list: str, broken_series_to_find):
    """ Finds the number of permutations that satisfy the check-list (returns 0 if none)"""

    check_list = [int(x) for x in literal_eval(check_list)]

    if len(input_chars) == 0 and len(check_list) == 0 and broken_series_to_find == 0:
        return 1
    if len(input_chars) == 0 or (input_chars[0] == "." and broken_series_to_find > 0):
        return 0

    curr_char = input_chars[0]
    input_chars = input_chars[1:]

    if (curr_char == "?" and broken_series_to_find > 0) or (curr_char == "#" and broken_series_to_find > 0):
        return find_number_permutations(
            input_chars, "#", str(check_list), broken_series_to_find-1)
    if curr_char == "?" and previous_char == "." and len(check_list) > 0:
        return find_number_permutations(
            input_chars, "#", str(check_list[1:]), check_list[0]-1) + find_number_permutations(
            input_chars, ".", str(check_list), 0)
    if curr_char == "?" or curr_char == ".":
        return find_number_permutations(
            input_chars, ".", str(check_list), 0)
    if curr_char == "#" and previous_char == "." and len(check_list) > 0:
        return find_number_permutations(
            input_chars, "#", str(check_list[1:]), check_list[0]-1)
    return 0


for line in open("Day12/input1.in", encoding="utf-8"):
    input_code = line.strip().split(" ")[0]
    check_code = [int(x) for x in line.strip().split(" ")[1].split(",")]

    RESULT1 += find_number_permutations(input_code, ".", str(check_code), 0)

    unfolded_input_code = input_code+"?"+input_code + \
        "?"+input_code+"?"+input_code+"?"+input_code

    unfolded_check_code = check_code+check_code+check_code+check_code+check_code
    RESULT2 += find_number_permutations(
        unfolded_input_code, ".", str(unfolded_check_code), 0)

print("Result1 ", RESULT1)
print("Result2 ", RESULT2)
