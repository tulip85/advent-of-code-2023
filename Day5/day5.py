input_file = open("Day5/input1.in", encoding="utf-8")

seeds_to_be_planted = []
seeds_to_be_planted_2 = []

index = ""
maps = {}
index_map = {}

results = {}


def return_value(item, map):
    return_val = item
    for triple_combi in map:
        if item <= triple_combi[1]+triple_combi[2] and item >= triple_combi[1]:
            return_val = triple_combi[0] + item-triple_combi[1]
    return return_val


def return_full_mapping(map):
    return_map = {}
    for triple_combi in map:
        for i in range(0, triple_combi[2]):
            return_map[triple_combi[1]+i] = triple_combi[0]+i
    return return_map


def intersect_maps(source, destination):
    return_map = []

    for sd, s, k in source:

        added = False

        for dd, d, m in destination:

            # print("------")
            # print("sd s k", sd, s, k)
            # print("dd d m", dd, d, m)

            # case 1: destination is encompassing entirely the source destination range
            if sd > d and sd+k < d+m:
                # print("case 1")
                operation = dd-d
                return_map.append((sd+operation, s, k))
                added = True
            # case 2: destination is covering a subset of the source destination range
            elif d >= sd and sd+k >= d+m:
                # print("case 2")
                s1 = d-sd+1
                s2 = m
                s3 = k-s2-s1

                if s1 > 0:
                    return_map.append((sd, s, s1))
                return_map.append((dd, s+s1, m))
                if s3 > 0:
                    return_map.append((d+m+1, (s+k)-s3, s3))
                added = True
            elif d <= sd and d+m <= sd+k and d+m >= sd:
                # print("case 3")
                s2 = (d+m)-sd
                s3 = k-s2

                if s2 > 0:
                    operation = dd-d
                    return_map.append((sd+operation, s, s2))
                if s3 > 0:
                    return_map.append((d+m+1, s+s2, s3))
                added = True
            elif sd <= d and sd+k <= d+m and sd+k >= d:
                # print("case 4")
                s1 = d-sd
                s2 = k-s1

                if s1 > 0:
                    return_map.append((sd, s, s1))
                if s2 > 0:
                    return_map.append((dd, s+s1, s2))

                added = True
        if not added:
            return_map.append((sd, s, k))

    return return_map


for line in input_file:
    if line[0:5] == "seeds":
        seeds_to_be_planted = line.split(":")[1].strip().split(" ")
        seeds_to_be_planted = [int(x) for x in seeds_to_be_planted]

        # for part two
        seed_range_to_be_planted_all = line.split(":")[1].strip().split(" ")
        item_1 = 0
        start_ranges = set()
        for i in range(0, len(seed_range_to_be_planted_all)):
            if i % 2 == 0:
                item_1 = seed_range_to_be_planted_all[i]
            else:
                start_ranges.add(
                    (int(item_1), int(item_1), int(seed_range_to_be_planted_all[i])))

        maps["start-to-seed"] = start_ranges

    elif ":" in line:
        index = line.split(" ")[0]
        index_map[index.split("-")[0]] = index.split("-")[2]
    elif line.strip() != "":
        map_item = line.strip().split(" ")
        if index in maps:
            maps[index].add(
                (int(map_item[0]), int(map_item[1]), int(map_item[2])))
        else:
            maps[index] = {(int(map_item[0]), int(
                map_item[1]), int(map_item[2]))}

index = "seed"

# part 1
for seed in seeds_to_be_planted:
    curr_val = seed
    index = "seed"
    while index in index_map:
        lookup_map_index = index+"-to-"+index_map[index]
        index = index_map[index]
        new_val = return_value(curr_val, maps[lookup_map_index])
        if seed in results:
            results[seed][index] = new_val
        else:
            results[seed] = {}
            results[seed][index] = new_val
        curr_val = new_val

LOWEST_LOCATION = -1
for result in results:
    result_set = results[result]
    if result_set["location"] < LOWEST_LOCATION or LOWEST_LOCATION == -1:
        LOWEST_LOCATION = result_set["location"]

print(LOWEST_LOCATION)

index = "seed"
index_map["start"] = "seed"
start_map = maps["start-to-seed"]
result_map = maps["start-to-seed"]
# part 2 - calculate all ranges and overlaps -> not yet working
while index in index_map:
    lookup_map_index = index+"-to-"+index_map[index]
    index = index_map[index]
    result_map = intersect_maps(result_map, maps[lookup_map_index])

min = -1
min_seed = 0
for x, y, z in result_map:
    if min < 0 or x < min:
        min = x
        min_seed = y
print(min, min_seed)
