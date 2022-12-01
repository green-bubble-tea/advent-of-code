import codecs
from collections import Counter

if __name__ == "__main__":
    vowels = ["a", "e", "i", "u", "o"]
    bad = ["ab", "cd", "pq", "xy"]
    count_vowels = lambda s: sum(s.count(i) for i in vowels)
    has_no_bad_pairs = lambda s: all(i not in s for i in bad)
    twice_char = lambda s: sum(1 for i, j in zip(s, s[1:]) if i == j)
    is_good_part_1 = lambda s: count_vowels(s) > 2 and has_no_bad_pairs(s) and twice_char(s) > 0

    one_letter_between = lambda s: len(["".join((i, j, k)) for i, j, k in zip(s, s[1:], s[2:]) if i == k]) > 0
    one_pair_twice = lambda s: any(s.count("".join([i, j])) > 1 for i, j in zip(s, s[1:]))

    is_good_part_2 = lambda s: one_pair_twice(s) and one_letter_between(s)

    with codecs.open("input.txt") as input_file:
        strings = list(map(str.strip, input_file.readlines()))
        print("part 1:", sum(map(is_good_part_1, strings)))

        print("part 2:", sum(map(is_good_part_2, strings)))
