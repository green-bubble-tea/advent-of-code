import codecs


def parse_line(line):
    tmp = line.strip().split(" ")
    return tmp[0], tmp[3], tmp[6], tmp[-2]


def calc_distance(reindeer, time):
    velocity, travel_time, rest_time = reindeer
    step = travel_time + rest_time
    full_flight = time // step
    partial_flight = min(travel_time, time - step * full_flight)
    return full_flight * travel_time * velocity + partial_flight * velocity


def calc_distance_with_points(reindeers, time):
    points = {i: 0 for i in reindeers}
    for second in range(1, time + 1):
        distances_dict = {i: calc_distance(j, second) for i, j in reindeers.items()}
        winner = max(distances_dict.values())
        for i in points:
            if distances_dict[i] == winner:
                points[i] += 1
    return points


if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        reindeers = {}
        for line in input_file.readlines():
            reindeer, *data = parse_line(line)
            reindeers[reindeer] = list(map(int, data))
        distances = {i: 0 for i in reindeers}
        for reindeer in reindeers:
            distances[reindeer] = calc_distance(reindeers[reindeer], 2503)
        print("part 1:", max(distances.values()))

        points_dict = calc_distance_with_points(reindeers, 2503)
        print("part 2:", max(points_dict.values()))


