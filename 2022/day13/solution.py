import codecs
from functools import cmp_to_key

if __name__ == "__main__":
    def compare(left_element, right_element):
        if isinstance(left_element, int) and isinstance(right_element, int):
            if left_element == right_element:
                return 0
            else:
                return left_element - right_element
        elif isinstance(left_element, list) and isinstance(right_element, list):
            element = list(zip(left_element, right_element))
            i = 0
            while i < len(element):
                i_left, i_right = element[i]
                cmp = compare(i_left, i_right)
                if cmp == 0:
                    i += 1
                else:
                    return cmp
            if len(left_element) == len(right_element):
                return 0
            else:
                return len(left_element) - len(right_element)
        elif isinstance(left_element, int) and isinstance(right_element, list):
            return compare([left_element], right_element)
        elif isinstance(left_element, list) and isinstance(right_element, int):
            return compare(left_element, [right_element])


    with codecs.open("input.txt") as input_file:
        contents = input_file.read()
        lines = list(map(lambda i: list(map(eval, i.split("\n"))), contents.split("\n\n")))
        right_sum = 0
        for index, line in enumerate(lines):
            left, right = line
            if compare(left, right) < 0:
                right_sum += index + 1
        print("part 1:", right_sum)
        lines.append([[[2]], [[6]]])
        flat_list = []
        for pair in lines:
            flat_list.append(pair[0])
            flat_list.append(pair[1])
        flat_list = sorted(flat_list, key=cmp_to_key(compare))
        print("part 2:", (flat_list.index([[2]]) + 1) * (flat_list.index([[6]]) + 1))
