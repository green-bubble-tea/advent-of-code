import codecs

if __name__ == "__main__":
    def get_neighbors(point, tab):
        x, y = point
        return list(filter(lambda p: 0 <= p[0] < len(tab) and 0 <= p[1] < len(tab[0]), [
            (x + 1, y),
            (x - 1, y),
            (x, y - 1),
            (x, y + 1)
        ]))


    def can_go(point1, point2, tab):
        x1, y1 = point1
        x2, y2 = point2
        return tab[x2][y2] - tab[x1][y1] <= 1


    def bfs(grid, start_point, end_point):
        queue = [[start_point]]
        seen = {start_point}
        while queue:
            path = queue.pop(0)
            if path[-1] == end_point:
                return path[:-1]
            for point in get_neighbors(path[-1], grid):
                if point not in seen and can_go(path[-1], point, grid):
                    if point == end_point:
                        return path
                    queue.append(path + [point])
                    seen.add(point)
        return []


    with codecs.open("input.txt") as input_file:
        E, S = ord("E"), ord("S")
        start, stop = (0, 0), (0, 0)
        starts = []
        lines = list(map(lambda i: list(map(ord, list(i.strip()))), input_file.readlines()))
        for dx, line in enumerate(lines):
            for dy, value in enumerate(line):
                if value == E:
                    stop = (dx, dy)
                    lines[dx][dy] = ord("z")
                if value == S:
                    start = (dx, dy)
                    starts.append(start)
                    lines[dx][dy] = ord("a")
                if chr(value) == "a":
                    starts.append((dx, dy))
        found_path = bfs(lines, start, stop)
        print("part 1:", len(found_path))
        shortest_path = 10_000
        for s in starts:
            found_path = len(bfs(lines, s, stop))
            if found_path > 0:
                shortest_path = min(found_path, shortest_path)
        print("part 2:", shortest_path)

