import codecs

if __name__ == "__main__":
    def parse_stacks(stacks_):
        stacks_dict = {i: [] for i in list(map(int, stacks_[-1].split()))}
        stacks_list = stacks_[:-1]
        for value in stacks_list:
            tmp = value.replace("   ", "[?]").replace("][", "] [").replace("  ", " ") + " "
            tmp += "[?] " * (len(stacks_dict) - tmp.count(" "))
            tmp = tmp.replace("]", "").replace("[", "")
            tmp = tmp.strip().split(" ")
            [stacks_dict[index + 1].insert(0, value) for index, value in enumerate(tmp) if value != "?"]
        return stacks_dict


    def parse_movements(movements_):
        movements_list = []
        for i in movements_:
            tmp = i.split(" ")
            move = (int(tmp[-3].strip()), int(tmp[-1]), int(tmp[1]))
            movements_list.append(move)
        return movements_list

    def move_crates(stacks_dict, movement_list, multiple=False):
        for move in movement_list:
            from_, to_, count_ = move
            elements = [stacks_dict[from_].pop() for _ in range(0, count_)]
            if not multiple:
                stacks_dict[to_].extend(elements)
            else:
                stacks_dict[to_].extend(elements[::-1])
        return stacks_dict


    with codecs.open("input.txt") as input_file:
        lines = list(map(str.rstrip, input_file.readlines()))
        s, m = lines[:lines.index("")], lines[lines.index("") + 1:]
        stacks = parse_stacks(s)
        movements = parse_movements(m)
        read_message = lambda sdict: "".join(i[-1] for i in sdict.values())

        new_stacks = move_crates(stacks, movements)
        message = read_message(new_stacks)
        print("part 1:", message)

        stacks = parse_stacks(s)
        new_stacks = move_crates(stacks, movements, multiple=True)
        message = read_message(new_stacks)
        print("part 2:", message)
