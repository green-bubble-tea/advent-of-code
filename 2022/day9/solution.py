import codecs

if __name__ == "__main__":

    directions = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, -1),
        "D": (0, 1)
    }


    def sign(a):
        return -1 if a < 0 else 0 if a == 0 else 1

    with codecs.open("input.txt") as input_file:
        lines = input_file.readlines()
        parse_line = lambda i: (i.strip().split(" ")[0], int(i.strip().split(" ")[1]))
        instructions = list(map(parse_line, lines))
        points = {(0, 0)}
        head_x, head_y = 0, 0
        tail_x, tail_y = 0, 0
        for i in range(len(lines)):
            direction, point = instructions[i]
            for _ in range(point):
                dx, dy = directions[direction]
                head_x += dx
                head_y += dy
                for _ in range(point):
                    delta_x = head_x - tail_x
                    delta_y = head_y - tail_y
                    if abs(delta_x) > 1 or abs(delta_y) > 1:
                        tail_x += sign(delta_x)
                        tail_y += sign(delta_y)
                    points.add((tail_x, tail_y))
        print("part 1:", len(points))
