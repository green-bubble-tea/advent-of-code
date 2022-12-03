import codecs

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
    # with codecs.open("input.txt") as input_file:
    #     lines = input_file.readlines()
    #     aunts = create_dict(lines)
    #     aunt = 0
    #     for key, value in aunts.items():
    #         if aunt_sue.items() >= value.items():
    #             aunt = key
    #     print("part 1:", aunt)
    #
    #     aunt = 0
    #     for key, value in aunts.items():
    #         value.update({i: 100 for i in sue_attributes if i not in value})
    #         for att_key, att_value in value.items():
    #             if att_key in good_keys and att_value == aunt_sue[att_key]:
    #                 if att_key in greater and att_value > aunt_sue[att_key]:
    #                     if att_key in fewer and att_value < aunt_sue[att_key]:
    #                         print(key)
    #                 # print(key)
    #                 # aunt = key
    #     print("part 2:", aunt)
    import re
    from operator import ge, le

    KNOWN = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }

    SPECIAL = {'cats': le, 'trees': le, 'pomeranians': ge, 'goldfish': ge}


    def is_real_aunt_parta(things, values):
        for thing, value in zip(things, values):
            if KNOWN[thing] != int(value):
                return False
        return True


    def is_real_aunt_partb(things, values):

        for special_thing, compare in SPECIAL.items():
            if special_thing in things:
                number_of_things = int(values.pop(things.index(special_thing)))
                things.remove(special_thing)
                if compare(number_of_things, KNOWN[special_thing]):
                    return False

        return is_real_aunt_parta(things, values)


    pattern = 'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)'
    for match in re.findall(pattern, open('input.txt').read()):
        num = match[0]
        things = list(match[1::2])
        values = list(match[2::2])

        if is_real_aunt_parta(things, values):
            print("Part A:", num)

        if is_real_aunt_partb(things, values):
            print("Part B", num)