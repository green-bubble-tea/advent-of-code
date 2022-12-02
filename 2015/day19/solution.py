import codecs

if __name__ == "__main__":
    def find_all(substring, string):
        first = string.find(substring)
        indexes = []
        while first != -1:
            indexes.append(first)
            first = string.find(substring, first + 1)
        return indexes


    def parse_rules(rules_string, part2=False):
        x = [i.split(" => ") for i in rules_string.split("\n")]
        if not part2:
            rdict = {}
            for i in x:
                from_, to_ = i
                if from_ in rdict:
                    rdict[from_].append(to_)
                else:
                    rdict[from_] = [to_]
            return rdict
        else:
            return {i[1]: i[0] for i in x}


    with codecs.open("input.txt") as input_file:
        rules, molecule = map(str.strip, input_file.read().split("\n\n"))
        rules_dict = parse_rules(rules)
        molecules = set()
        for key, value in rules_dict.items():
            all_finds = find_all(key, molecule)
            for index in all_finds:
                for v in value:
                    next_index = index + len(key)
                    candidate = f"{molecule[:index]}{v}{molecule[next_index:]}"
                    molecules.add(candidate)
        print("part 1:", len(molecules))
        step = 0
        rules_dict_2 = parse_rules(rules, part2=True)
        rules_dict_2 = dict(sorted(rules_dict_2.items(), key=lambda i: len(i[0]), reverse=True))
        while molecule != "e":
            for key, value in rules_dict_2.items():
                if key in molecule:
                    molecule = molecule.replace(key, value, 1)
                    step += 1
        print("part 2:", step)
