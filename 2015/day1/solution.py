import codecs

if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        input_string = input_file.read().strip()
        delta = input_string.count("(") - input_string.count(")")
        print("part 1:", delta)
        index, first, found = 0, 0, False
        while index < len(input_string) and not found:
            if input_string[index] == "(":
                first += 1
            else:
                first -= 1
                if first == -1:
                    first = index
                    found = True
            index += 1
        print("part 2:", first)
