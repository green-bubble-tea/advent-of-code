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
good_keys = [i for i in aunt_sue.keys() if i not in greater + fewer]


def parse_line(line):
    tmp = line.strip().replace(":", "").replace(",", "").split(" ")
    sue_id = int(tmp[1])
    attributes = {}
    for index in range(2, len(tmp) - 1, 2):
        attribute, count = tmp[index], int(tmp[index + 1])
        attributes.update({attribute: count})
    return {sue_id: attributes}


def create_dict(lines):
    s = [parse_line(line) for line in lines]
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

        aunt = 0
        for key, value in aunts.items():
            for att_key, att_value in value.items():
                if att_key in good_keys and att_value == aunt_sue[att_key]:
                    if att_key in greater and att_value < aunt_sue[att_key]:
                        print(key)
                    # print(key)
                    # aunt = key

        print("part 2:", aunt)
