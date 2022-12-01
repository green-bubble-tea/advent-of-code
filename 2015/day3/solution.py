import codecs

if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        def update_grid(grid, direction, santa_position):
            x, y = santa_position
            grid[x][y] += 1
            if direction == "^":
                if x - 1 < 0:
                    grid.insert(0, [0 for _ in range(1000)])
                x -= 1
            elif direction == "v":
                if x + 1 > len(grid):
                    grid.append([0 for _ in range(1000)])
                x += 1
            elif direction == ">":
                if y + 1 > len(grid[start_x]):
                    grid[x].append(0)
                y += 1
            elif direction == "<":
                if y - 1 < 0:
                    grid[x].insert(0, 0)
                y -= 1
            grid[x][y] += 1
            return x, y

        directions = list(input_file.read())
        positive_houses = lambda x: len(list(filter(lambda i: i > 0, x)))

        grid_1 = [[0 for i in range(1000)] for j in range(1000)]
        start_x, start_y = 500, 500
        for i in directions:
            start_x, start_y = update_grid(grid_1, i, (start_x, start_y))
        print("part 1:", sum(map(positive_houses, grid_1)))

        grid_2 = [[0 for i in range(1000)] for j in range(1000)]
        santa_x, santa_y, robo_x, robo_y = 500, 500, 500, 500
        for i in range(0, len(directions), 2):
            santa, robo = directions[i], directions[i + 1]
            santa_x, santa_y = update_grid(grid_2, santa, (santa_x, santa_y))
            robo_x, robo_y = update_grid(grid_2, robo, (robo_x, robo_y))
        print("part 2:", sum(map(positive_houses, grid_2)))



