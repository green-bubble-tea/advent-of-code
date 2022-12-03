import codecs

if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        lines = list(map(str.strip, input_file.readlines()))
        calc_priority = lambda x: ord(x) - 96 if ord(x) in range(97, 123) else ord(x) - 38
        rucksack = list(map(lambda i: (i[:len(i) // 2], i[len(i) // 2:].strip()), lines))
        items = list(map(lambda i: set(i[0]).intersection(set(i[1])), rucksack))
        priority_sum = sum(map(lambda i: sum(map(calc_priority, i)), items))
        print("part 1:", priority_sum)
        groups = [lines[i:i+3] for i in range(0, len(lines), 3)]
        tags = map(lambda i: "".join(set(i[0]).intersection(*i[1:])), groups)
        tags_sum = sum(map(calc_priority, tags))
        print("part 2:", tags_sum)
