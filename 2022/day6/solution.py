import codecs


def process_marker(string, distinct_number):
    all_different = lambda s: all(s.count(i) == 1 for i in s)
    index, marker_found = 0, False
    while index < len(string) - distinct_number and not marker_found:
        substr = string[index:index + distinct_number]
        if all_different(substr):
            marker_found = True
        else:
            index += 1
    return index + distinct_number


if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        message = input_file.read().strip()
        print("part 1:", process_marker(message, 4))
        print("part 1:", process_marker(message, 14))
