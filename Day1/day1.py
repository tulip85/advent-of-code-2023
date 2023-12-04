input_file = open("Day1/input1.in", encoding="utf-8")

number_mapping = {"one": "1", "two": "2", "three": "3", "four": "4",
                  "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

first_chars = set([x[0] for x in number_mapping])
lookup_table = {"o": ["one"], "t": ["two", "three"], "f": [
    "four", "five"], "s": ["six", "seven"], "e": ["eight"], "n": ["nine"]}

RESULT_1 = 0
RESULT_2 = 0

for line in input_file:

    parsed_line = []
    parsed_line_digits = []

    POS = 0
    for char in line:
        if char.isdigit():
            parsed_line.append(char)
            parsed_line_digits.append(char)
        elif char in first_chars:
            # potentially a number
            for number in lookup_table[char]:
                if len(line) >= len(number)+POS and line[POS:len(number)+POS] == number:
                    parsed_line.append(number_mapping[number])

        POS += 1

    RESULT_1 = RESULT_1 + \
        int(parsed_line_digits[0]+"" +
            parsed_line_digits[len(parsed_line_digits)-1])
    RESULT_2 = RESULT_2 + \
        int(parsed_line[0]+""+parsed_line[len(parsed_line)-1])

print("Result 1", RESULT_1)
print("Result 2", RESULT_2)
