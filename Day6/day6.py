input_file = open("Day6/input1.in", encoding="utf-8")

times_1 = input_file.readline().split()
distances_1 = input_file.readline().split()

times_1.remove("Time:")
distances_1.remove("Distance:")

times_2 = [int(''.join(times_1))]
distances_2 = [int(''.join(distances_1))]

times_1 = [int(x) for x in times_1]
distances_1 = [int(x) for x in distances_1]


def get_distance(button_time, total_time):
    return (total_time-button_time)*button_time


def get_result(times, distances):
    result = 1

    for i in range(0, len(times)):
        time = times[i]
        distance = distances[i]

        winning_combos = 0

        for t in range(0, time+1):
            if get_distance(t, time) > distance:
                winning_combos += 1

        result *= winning_combos
    return result


print("Result 1", get_result(times_1, distances_1))
print("Result 2", get_result(times_2, distances_2))
