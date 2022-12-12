import codecs
from functools import reduce
import copy

if __name__ == "__main__":

    def monkey_business(monkeys_dict, rounds, divide=True):
        monkey_copy = copy.deepcopy(monkeys_dict)
        tests = [i["test"] for i in monkey_copy.values()]
        lcm = reduce(lambda x, y: x * y, tests)
        for _ in range(rounds):
            for value in monkey_copy.values():
                while value["starting_items"]:
                    item = value["starting_items"].pop(0)
                    operator = value["operation"].replace("old", str(item))
                    worry_level = eval(operator)
                    worry_level = worry_level // 3 if divide else worry_level
                    test_result = str(worry_level % value["test"] == 0)
                    next_monkey_id = value[f"{test_result}_monkey_id"]
                    if not divide and worry_level > lcm:
                        worry_level = worry_level % lcm
                    monkey_copy[next_monkey_id]["starting_items"].append(worry_level)
                    value["items_inspected"] += 1
        top_items_inspected = sorted([i["items_inspected"] for i in monkey_copy.values()], reverse=True)[:2]
        return reduce(lambda x, y: x * y, sorted(top_items_inspected, reverse=True)[:2])


    with codecs.open("input.txt") as input_file:
        lines = list(map(str.strip, input_file.read().split("\n\n")))
        monkeys = {i: {} for i in range(len(lines))}
        for i in lines:
            attributes = list(map(str.strip, i.split("\n")))
            monkey_id = int(attributes[0].split(" ")[-1][:-1])
            starting_items = attributes[1].strip().replace(":", "").replace(",", "").split(" ")[2:]
            operation = "".join(attributes[2].strip().split(" ")[3:])
            test = int(attributes[3].strip().split(" ")[-1])
            true_monkey_id = int(attributes[4].strip().split(" ")[-1])
            false_monkey_id = int(attributes[5].strip().split(" ")[-1])
            monkeys[monkey_id] = {
                "starting_items": starting_items,
                "operation": operation,
                "test": test,
                "True_monkey_id": true_monkey_id,
                "False_monkey_id": false_monkey_id,
                "items_inspected": 0
            }

        print("part 1:", monkey_business(monkeys, 20))
        print("part 2:", monkey_business(monkeys, 10_000, divide=False))

