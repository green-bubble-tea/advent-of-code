import codecs
from itertools import permutations
import sys


def parse_input(line):
    tmp = line.strip().split(" ")
    person, next_person = tmp[0], tmp[-1][:-1]
    happiness = int(tmp[3]) if tmp[2] == "gain" else -int(tmp[3])
    return person, next_person, happiness


def calc_happiness(seating):
    happiness = 0
    for i, j in zip(seating, seating[1:]):
        happiness += happiness_dict[(i, j)] + happiness_dict[(j, i)]
    last_x, last_y = seating[-1], seating[0]
    happiness += happiness_dict[(last_x, last_y)] + happiness_dict[(last_y, last_x)]
    return happiness


def max_happiness(seatings):
    max_happy = -sys.maxsize - 1
    for i in seatings:
        happiness = calc_happiness(i)
        if happiness > max_happy:
            max_happy = happiness
    return max_happy


if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        data = list(map(parse_input, input_file.readlines()))
        happiness_dict = {}
        people = set()
        for i in data:
            x, y, happy = i
            people.add(x)
            people.add(y)
            happiness_dict[(x, y)] = happy
        seatings = map(list, permutations(people))
        print("part 1:", max_happiness(seatings))
        people.add("me")
        seatings = map(list, permutations(people))
        for i in people:
            happiness_dict[(i, "me")] = 0
            happiness_dict[("me", i)] = 0
        print("part 2:", max_happiness(seatings))
