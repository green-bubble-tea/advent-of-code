import codecs

if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        lines = list(map(lambda line: sum(map(int, line.split("\n"))), input_file.read().split("\n\n")))
        top_3 = sum(sorted(lines, reverse=True)[:3])
        print("part 1:", max(lines))
        print("part 2:", top_3)
