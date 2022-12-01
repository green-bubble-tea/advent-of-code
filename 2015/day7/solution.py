import codecs

if __name__ == "__main__":

    def simulate(electrode_dict, computed):
        while electrode_dict:
            new_key, new_value = "", ""
            for key, value in electrode_dict.items():
                operation_string = ""
                for i in value:
                    if i in computed:
                        operation_string += f"{computed[i]}"
                    if i in actions:
                        operation_string += actions[i]
                    if i.isdigit():
                        operation_string += i
                try:
                    new_value = eval(operation_string)
                    new_key = key
                except SyntaxError:
                    ...  # not the right one
            if new_key:
                computed[new_key] = new_value
                electrode_dict.pop(new_key)

    def parse_line(electrode_dict, line):
        from_el, to_el = line.split(" -> ")
        try:
            electrode_dict[to_el] = int(from_el)
        except ValueError:
            electrode_dict[to_el] = from_el.split()


    def find_numeric(electrode_dict):
        numericals = {}
        for i, j in electrode_dict.items():
            if isinstance(j, int):
                numericals[i] = j
        [electrode_dict.pop(i) for i in numericals]
        return numericals


    with codecs.open("input.txt") as input_file:
        f = input_file.readlines()
        actions = {
            "AND": "&",
            "OR": "|",
            "NOT": "~",
            "RSHIFT": ">>",
            "LSHIFT": "<<",
            "XOR": "^"
        }
        electrode_dict_1, electrode_dict_2 = {}, {}
        [parse_line(electrode_dict_1, i.strip()) for i in f]
        [parse_line(electrode_dict_2, i.strip()) for i in f]
        already_computed_1, already_computed_2 = find_numeric(electrode_dict_1), find_numeric(electrode_dict_2)

        simulate(electrode_dict_1, already_computed_1)
        computed_a = already_computed_1["a"]
        print("part 1:", computed_a)
        already_computed_2["b"] = already_computed_1["a"]
        simulate(electrode_dict_2, already_computed_2)
        print(already_computed_2["a"])