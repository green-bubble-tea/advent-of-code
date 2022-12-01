import json
import codecs
import re

sum_numbers = lambda string: sum(map(int, re.findall(r'-?\d+', string)))


def sum_item(root):
    if isinstance(root, int):
        return root
    if isinstance(root, list):
        return sum(map(sum_item, root))
    if isinstance(root, dict):
        if "red" in root.values():
            return 0
        return sum(map(sum_item, root.values()))
    else:
        return 0


if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        data_1 = input_file.read()
        print("part 1:", sum_numbers(data_1))
        data_2 = json.loads(data_1)
        print("part 2:", sum_item(data_2))
