import codecs
from itertools import combinations
from functools import reduce


def parse_line(line):
    return sorted(list(map(int, line.split("x"))))


def count_paper(line):
    fields = list(combinations(line, 2))
    surface = lambda x, y: x * y
    return sum(2 * surface(*i) for i in fields) + surface(*fields[0])


def count_ribbon(line):
    ribbon = reduce(lambda x, y: x * y, line)
    bow = 2 * sum(line[:2])
    return ribbon + bow


if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        lines = list(map(parse_line, input_file.readlines()))
        print("part 1: ", sum(count_paper(i) for i in lines))
        print("part 2: ", sum(count_ribbon(i) for i in lines))
