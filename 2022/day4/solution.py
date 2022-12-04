import codecs


def parse_line(line):
    range1, range2 = list(map(lambda i: list(map(int, i.split("-"))), line.split(",")))
    set_range = lambda i: set(range(i[0], i[1] + 1))
    return set_range(range1), set_range(range2)


if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        lines = list(map(str.strip, input_file.readlines()))
        ranges_1 = map(parse_line, lines)
        ranges_2 = map(parse_line, lines)
        is_subset = lambda s1, s2: s1.issubset(s2) or s2.issubset(s1)
        overlaps = lambda s1, s2: len(s1.intersection(s2)) != 0
        print("part 1:", len(list(filter(lambda i: is_subset(i[0], i[1]), ranges_1))))
        print("part 2:", len(list(filter(lambda i: overlaps(i[0], i[1]), ranges_2))))
