from functools import cache
from ast import literal_eval


RESULT1 = 0
RESULT2 = 0

input_file = open("Day12/input1.in", encoding="utf-8")


@cache
def find_number_permutations(input_chars, previous_char, check_list: str, broken_series_to_find):
    check_list = [int(x) for x in literal_eval(check_list)]

    previous_char_dot = True if previous_char == "." else False

    if len(input_chars) == 0:
        if len(check_list) == 0 and broken_series_to_find == 0:
            return 1
        else:
            return 0

    curr_char = input_chars[0]
    input_chars = input_chars[1:]

    # if a question mark, decide based on the previous character
    if curr_char == "?":
        if broken_series_to_find > 0:
            return find_number_permutations(
                input_chars, "#", str(check_list), broken_series_to_find-1)
        elif previous_char_dot and len(check_list) > 0:
            broken = find_number_permutations(
                input_chars, "#", str(check_list[1:]), check_list[0]-1)
            functioning = find_number_permutations(
                input_chars, ".", str(check_list), 0)

            return functioning + broken
        else:
            return find_number_permutations(
                input_chars, ".", str(check_list), 0)

    # if a # and previous is a dot, then start a new check, otherwise, return 0
    elif curr_char == "#":
        if broken_series_to_find > 0:
            return find_number_permutations(
                input_chars, "#", str(check_list), broken_series_to_find-1)
        if previous_char_dot and len(check_list) > 0:
            return find_number_permutations(
                input_chars, "#", str(check_list[1:]), check_list[0]-1)
        else:
            return 0

    # if a dot, just continue with the next item
    if curr_char == ".":
        if broken_series_to_find > 0:
            return 0
        else:
            return find_number_permutations(
                input_chars, ".", str(check_list), 0)


for line in input_file:
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
