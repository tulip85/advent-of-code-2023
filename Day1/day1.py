import re

input = open("Day1/input1.in")

number_mapping = {"one": "1", "two": "2", "three": "3", "four": "4",
                  "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

first_chars = ["o", "t", "f", "s", "e", "n"]
lookup_table = {"o": ["one"], "t": ["two", "three"], "f": [
    "four", "five"], "s": ["six", "seven"], "e": ["eight"], "n": ["nine"]}

result = 0

for line in input:

    parsed_line = []

    pos = 0
    for char in line:
        if char.isdigit():
            parsed_line.append(char)
        elif char in first_chars:
            # potentially a number
            for number in lookup_table[char]:
                if len(line) >= len(number)+pos and line[pos:len(number)+pos] == number:
                    parsed_line.append(number_mapping[number])

        pos = pos+1

    number = int(parsed_line[0]+""+parsed_line[len(parsed_line)-1])
    result = result + number

print(result)
