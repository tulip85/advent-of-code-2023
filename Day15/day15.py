
BOXES = {}

for i in range(0, 256):
    BOXES[i] = []


def hashString(input_str) -> int:

    result = 0
    for c in input_str:
        ascii_code = ord(c)

        result += ascii_code

        result *= 17
        result = result % 256
    return result


def get_focusing_power(box_number, slot_number, fc_len) -> int:
    return (1+box_number)*(slot_number+1)*fc_len


def return_item_in_box(label_hash, label):
    item = [item for item in BOXES[label_hash] if item[0] == label]
    if len(item) > 0:
        return item[0]
    else:
        return None


def return_item_index_in_box(label_hash, label):
    item = return_item_in_box(label_hash, label)
    if item in BOXES[label_hash]:
        return BOXES[label_hash].index(item)
    else:
        return None


RESULT1 = 0

for line in open("Day15/input1.in", encoding="utf-8"):

    for string_in in line.split(","):

        if "=" in string_in:
            label = string_in.split("=")[0]
            label_hash = hashString(label)
            focal_length = string_in.split("=")[1]
            existing_item_index = return_item_index_in_box(label_hash, label)
            new_item = (label, focal_length)
            if existing_item_index is not None:
                BOXES[label_hash][existing_item_index] = new_item
            else:
                BOXES[label_hash].append(new_item)

        else:
            label = string_in.split("-")[0]
            label_hash = hashString(label)
            existing_item_index = return_item_index_in_box(label_hash, label)
            if existing_item_index is not None:
                BOXES[label_hash].pop(
                    existing_item_index)

        RESULT1 += hashString(string_in)

RESULT2 = 0
for box in range(0, 256):
    slot = 0
    for lens in BOXES[box]:
        RESULT2 += get_focusing_power(box, slot, int(lens[1]))
        slot += 1

print("Result 1", RESULT1)
print("Result 2", RESULT2)

# too high: 357556
