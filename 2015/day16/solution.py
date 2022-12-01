import codecs
import random

aunt_sue = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

sue_attributes = [
    "children",
    "cats",
    "samoyeds",
    "pomeranians",
    "akitas",
    "vizslas",
    "goldfish",
    "trees",
    "cars",
    "perfumes"
]

greater = ["cats", "trees"]
fewer = ["pomeranians", "goldfish"]
wrong_keys = ["cats", "trees", "pomeranians", "goldfish"]
# good_keys = [i for i in sue_attributes if i not in wrong_keys]


def parse_line(line, part2=False):
    tmp = line.strip().replace(":", "").replace(",", "").split(" ")
    sue_id = int(tmp[1])
    attributes = {} if not part2 else {i: 1 for i in sue_attributes}
    for index in range(2, len(tmp) - 1, 2):
        attribute, count = tmp[index], int(tmp[index + 1])
        attributes.update({attribute: count})
    return {sue_id: attributes}


def create_dict(lines, part2=False):
    s = [parse_line(line, part2) for line in lines]
    sues_dict = {}
    [sues_dict.update(i) for i in s]
    return sues_dict


def filter_aunt(aunt_attributes):
    return aunt_attributes["cats"] < aunt_sue["cats"] \
           and aunt_attributes["trees"] < aunt_sue["trees"] \
           and aunt_attributes["pomeranians"] > aunt_sue["pomeranians"] \
           and aunt_attributes["goldfish"] > aunt_sue["goldfish"]


if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        lines = input_file.readlines()
        aunts = create_dict(lines)
        aunt = 0
        for key, value in aunts.items():
            if aunt_sue.items() >= value.items():
                aunt = key
        print("part 1:", aunt)

        aunts = create_dict(lines, True)
        aunts = {i: j for i, j in aunts.items() if filter_aunt(j)}
        [aunt_sue.pop(i) for i in wrong_keys]
        aunt = 0
        for key, value in aunts.items():
            print(value)
            if aunt_sue.items() >= value.items():
                aunt = key

        print("part 2:", aunt)

