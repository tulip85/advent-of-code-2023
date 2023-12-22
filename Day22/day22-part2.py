import copy
BLOCK_REGISTRY = {}
IS_SUPPORTING = {}


COORDINATE_REGISTRY = {}
Z_LAYER_MAP = {}
SUPPORTED_BY = {}

BLOCK_ID = 0
for line in open("Day22/input1.in", encoding="utf-8"):

    blocks = line.strip().split("~")
    start = [int(i) for i in blocks[0].split(",")]
    end = [int(i) for i in blocks[1].split(",")]
    BLOCK_REGISTRY[BLOCK_ID] = (start, end)

    COORDINATE_REGISTRY[BLOCK_ID] = []
    IS_SUPPORTING[BLOCK_ID] = set()
    SUPPORTED_BY[BLOCK_ID] = set()

    if (start[0] == end[0]):
        if (start[1] == end[1]):
            for z in range(min(start[2], end[2]), max(start[2], end[2])+1):
                COORDINATE_REGISTRY[BLOCK_ID].append(
                    (start[0], start[1], z))

        else:
            for y in range(min(start[1], end[1]), max(start[1], end[1])+1):
                COORDINATE_REGISTRY[BLOCK_ID].append(
                    (start[0], y, start[2]))
    else:
        for x in range(min(start[0], end[0]), max(start[0], end[0])+1):
            COORDINATE_REGISTRY[BLOCK_ID].append((x, start[1], start[2]))

    BLOCK_ID += 1

print("loaded")


def is_coord_below_occupied(coordinates, block_id, coord_registry):
    all_coordinates_temp = list(coord_registry.values())

    all_coordinates = []
    for t in all_coordinates_temp:
        all_coordinates += t

    for coord in coord_registry[block_id]:
        all_coordinates.remove(coord)

    for coord in coordinates:
        if (coord[0], coord[1], coord[2]-1) in all_coordinates or coord[2] <= 1:
            return True

    return False


def make_blocks_fall():
    SORTING = True
    SORTED = False
    while SORTING:
        SORTING = False
        for b_id in range(0, BLOCK_ID):
            if not is_coord_below_occupied(COORDINATE_REGISTRY[b_id], b_id, COORDINATE_REGISTRY):
                # move the block one down
                old_coordinates = COORDINATE_REGISTRY[b_id]
                new_coordinates = []
                for coord in old_coordinates:
                    new_coordinates.append((coord[0], coord[1], coord[2]-1))
                    SORTING = True
                    SORTED = True
                COORDINATE_REGISTRY[b_id] = new_coordinates
    return SORTED


def simulate_blocks_fall(block_to_remove):
    coord_reg = copy.deepcopy(COORDINATE_REGISTRY)
    del coord_reg[block_to_remove]
    SORTING = True
    SORTED = False
    elements_moved = set()

    while SORTING:
        SORTING = False
        for b_id in coord_reg.keys():
            if not is_coord_below_occupied(coord_reg[b_id], b_id, coord_reg):
                # move the block one down
                old_coordinates = coord_reg[b_id]
                new_coordinates = []
                for coord in old_coordinates:
                    new_coordinates.append((coord[0], coord[1], coord[2]-1))
                    SORTING = True
                    SORTED = True
                coord_reg[b_id] = new_coordinates
                if old_coordinates != new_coordinates:
                    elements_moved.add(b_id)
    return len(elements_moved)


make_blocks_fall()

for b_id in range(0, BLOCK_ID):

    for block in COORDINATE_REGISTRY[b_id]:
        # find a block in the same coordinates with a higher z
        for coord in COORDINATE_REGISTRY:
            if coord != b_id:
                potential = set()
                for cand_coord in COORDINATE_REGISTRY[coord]:
                    if cand_coord[0] == block[0] and cand_coord[1] == block[1] and cand_coord[2] == block[2]-1:
                        potential.add(coord)
                if len(potential) > 1:
                    print("need to deal with this")
                elif len(potential) == 1:
                    elem = potential.pop()
                    IS_SUPPORTING[elem].add(b_id)
                    SUPPORTED_BY[b_id].add(elem)


RESULT2 = 0
for b_id in range(0, BLOCK_ID):

    RESULT2 += simulate_blocks_fall(b_id)


print("Can fall", RESULT2)
