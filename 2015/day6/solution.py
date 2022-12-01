import codecs
from collections import Counter

if __name__ == "__main__":
    def parse_line(line):
        f = line.split()
        return f[-4], list(map(int, f[-3].split(","))), list(map(int, f[-1].split(",")))

    def toggle_map(lights_map, part1=True):
        for i in instructions:
            action = i[0]
            start_x, end_x = i[1][0], i[2][0] + 1
            start_y, end_y = i[1][1], i[2][1] + 1
            for dx in range(start_x, end_x):
                for dy in range(start_y, end_y):
                    if action == "on":
                        if not part1:
                            lights_map[dx][dy] += 1
                        else:
                            lights_map[dx][dy] = 1
                    elif action == "off":
                        if not part1:
                            if lights_map[dx][dy] > 0:
                                lights_map[dx][dy] -= 1
                            # print(lights_map[dx][dy])
                        else:
                            lights_map[dx][dy] = 0
                    else:
                        if not part1:
                            lights_map[dx][dy] += 2
                        else:
                            lights_map[dx][dy] = int(not lights_map[dx][dy])
        return sum(map(lambda x: sum(x), lights_map))


    with codecs.open("input.txt") as input_file:
        instructions = list(map(parse_line, input_file.readlines()))
        print("part 1:", toggle_map([[0 for x in range(1000)] for y in range(1000)]))
        print("part 2:", toggle_map([[0 for x in range(1000)] for y in range(1000)], False))
