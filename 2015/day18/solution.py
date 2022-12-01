import codecs

ON, OFF = "#", "."

if __name__ == "__main__":
    def grid_to_string(lights):
        return "\n".join(map(lambda i: "".join(i), lights))


    def on_lights_count(lights):
        return sum(map(lambda i: i.count(ON), lights))


    def is_corner(point, lights):
        # corner = [(0, 0), (0, len(lights[0]) - 1), (len(lights) - 1, 0), (len(lights) - 1, len(lights[0]) - 1)]
        return point in [(0, 0), (0, len(lights[0]) - 1), (len(lights) - 1, 0), (len(lights) - 1, len(lights[0]) - 1)]


    def on_neighbors_count(point, lights):
        x, y = point
        candidate_points = list(filter(lambda i: 0 <= i[0] < len(lights) and 0 <= i[1] < len(lights[0]),
                                       [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                                        (x + 1, y - 1), (x + 1, y), (x + 1, y + 1),
                                        (x, y - 1), (x, y + 1)]))
        return len(list(filter(lambda i: lights[i[0]][i[1]] == ON, candidate_points)))


    def toggle_lights(step, max_step, lights, part):
        if step < max_step:
            step_grid = [["." for _ in lights[0]] for _ in lights]
            for x_index, x_value in enumerate(lights):
                for y_index, y_value in enumerate(x_value):
                    on_count = on_neighbors_count((x_index, y_index), lights)
                    if part == 1 or part == 2 and not is_corner((x_index, y_index), step_grid):
                        if y_value == ON:
                            step_grid[x_index][y_index] = ON if on_count in [2, 3] else OFF
                        else:
                            step_grid[x_index][y_index] = ON if on_count == 3 else OFF
                    else:
                        step_grid[x_index][y_index] = ON
            if step == max_step - 1:
                print(f"part {part}: {on_lights_count(step_grid)}")
            toggle_lights(step + 1, max_step, step_grid, part)


    with codecs.open("input.txt") as input_file:
        lines = input_file.readlines()
        grid = list(map(lambda i: list(i.strip()), lines))
        grid_2 = list(map(lambda i: list(i.strip()), lines))
        toggle_lights(0, 100, grid, 1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if is_corner((i, j), grid):
                    grid_2[i][j] = ON
                else:
                    grid_2[i][j] = grid[i][j]
        toggle_lights(0, 100, grid_2, 2)
