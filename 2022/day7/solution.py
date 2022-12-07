import codecs


def update(path, value, dictionary):
    if len(path) == 1:
        if path[0] in dictionary:
            dictionary[path[0]].update(value)
        else:
            dictionary[path[0]] = value
    else:
        update(path[1:], value, dictionary[path[0]])
    return dictionary


def update_sum(path, value, dictionary):
    if "sum" in dictionary[path[0]]:
        dictionary[path[0]]["sum"] += value
    else:
        dictionary[path[0]]["sum"] = value
    if len(path) > 1:
        update_sum(path[1:], value, dictionary[path[0]])


def filter_tree(dictionary, min_value, max_value, values):
    for k, v in dictionary.items():
        if isinstance(v, int):
            if k == "sum" and min_value < v < max_value:
                values.append(v)
        else:
            filter_tree(dictionary[k], min_value, max_value, values)


if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        lines = list(map(str.strip, input_file.readlines()))
        tree = {}
        paths = set()
        current_path = []
        for line in lines:
            tmp = line.split(" ")
            if line.startswith("$ cd"):
                if not line.endswith(".."):
                    current_path.append(tmp[-1])
                else:
                    current_path.pop()
            elif line.startswith("$ ls"):
                continue
            else:
                a, b = tmp
                paths.add(tuple(current_path))
                if a == "dir":
                    tree = update(current_path, {b: {}}, tree)
                    update_sum(current_path, 0, tree)
                else:
                    tree = update(current_path, {b: int(a)}, tree)
                    update_sum(current_path, int(a), tree)

        at_most = 100000
        filtered_dirs = []
        filter_tree(tree, 0, at_most, filtered_dirs)
        print("part 1:", sum(filtered_dirs))

        max_space, min_unused_space = 70000000, 30000000
        unused_space = max_space - tree["/"]["sum"]
        needs_freeing = min_unused_space - unused_space
        filtered_dirs = []
        filter_tree(tree, needs_freeing, max_space, filtered_dirs)
        print("part 2:", min(filtered_dirs))

