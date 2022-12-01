import codecs
from itertools import combinations

if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        vessels = list(map(int, input_file.readlines()))
        target = 150
        vessels_lengths = []
        vessel_count = 0
        for i in range(len(vessels) + 1):
            vessels_combinations = list(filter(lambda v: sum(v) == target, combinations(vessels, i)))
            if vessels_combinations:
                vessels_lengths += list(map(len, vessels_combinations))
            vessel_count += len(vessels_combinations)
        print("part 1:", vessel_count)
        print("part 2:", vessels_lengths.count(min(vessels_lengths)))


