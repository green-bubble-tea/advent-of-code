import codecs


def is_visible(tree, trees):
    x, y = tree
    top = all(trees[i][y] < trees[x][y] for i in range(0, x))
    bottom = all(trees[i][y] < trees[x][y] for i in range(x + 1, len(trees)))
    right = all(trees[x][i] < trees[x][y] for i in range(y + 1, len(trees[0])))
    left = all(trees[x][i] < trees[x][y] for i in range(0, y))
    return any((top, bottom, right, left))


def calc_scenic(trees_list, point, trees):
    index = 0
    scenic = 0
    x, y = point
    is_blocking = False
    while index < len(trees_list) and not is_blocking:
        scenic += 1
        if trees[x][y] > trees_list[index]:
            index += 1
        else:
            is_blocking = True
    return scenic


def scenic_view(tree, trees):
    x, y = tree
    top = calc_scenic([trees[i][y] for i in range(0, x)][::-1], tree, trees)
    bottom = calc_scenic([trees[i][y] for i in range(x + 1, len(trees))], tree, trees)
    right = calc_scenic([trees[x][i] for i in range(y + 1, len(trees[0]))], tree, trees)
    left = calc_scenic([trees[x][i] for i in range(0, y)][::-1], tree, trees)
    return top * bottom * right * left


if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        lines = input_file.readlines()
        grid = list(map(lambda i: list(map(int, list(i.strip()))), lines))
        max_scenic = 1
        visible = 2 * (len(grid) - 1) + 2 * (len(grid[0]) - 1)
        for row in range(1, len(grid) - 1):
            for column in range(1, len(grid[0]) - 1):
                if is_visible((row, column), grid):
                    visible += 1
                max_scenic = max(scenic_view((row, column), grid), max_scenic)
        print("part 1:", visible)
        print("part 2:", max_scenic)
