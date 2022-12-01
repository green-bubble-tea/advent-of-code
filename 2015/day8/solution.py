import codecs

if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        def x(s):
            r = s.translate(str.maketrans({"-": r"\-",
                                           "]": r"\]",
                                           "\\": r"\\",
                                           "^": r"\^",
                                           "$": r"\$",
                                           "*": r"\*",
                                           ".": r"\.",
                                           "\"": r"\""}))
            return len(r) + 2


        count_all = lambda s: len(codecs.decode(s, "unicode-escape")) - 2
        count_raw = lambda s: len(s) - count_all(s)
        f = list(map(str.strip, input_file.readlines()))
        print("part 1:", sum(map(count_raw, f)))
        count_enc = lambda s: x(s) - len(s)
        print("part 2:", sum(map(count_enc, f)))
