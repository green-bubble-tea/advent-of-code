import codecs

if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        input_string = input_file.read().strip()
        delta = input_string.count("(") - input_string.count(")")
        print("part 1:", delta)
        f = 0
        print(input_string.find(")"))
        # for index, character in enumerate(input_string):
        #     if character == "(":
        #         f += 1
        #     else:
        #         f -= 1
        #         if f < 0:
        #             print(index + 1)
