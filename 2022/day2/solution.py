import codecs

if __name__ == "__main__":
    winning_pairs = [("A", "Y"), ("B", "Z"), ("C", "X")]
    ties = [("A", "X"), ("B", "Y"), ("C", "Z")]
    losing_pairs = [("A", "Z"), ("B", "X"), ("C", "Y")]

    def calculate_result(game_round):
        result = dict(X=1, Y=2, Z=3)[game_round[1]]
        if game_round in winning_pairs:
            result += 6
        elif game_round in ties:
            result += 3
        else:
            result += 0
        return result


    def play_2(game_round):
        opponent, result = game_round
        get_pair = lambda tab: "".join(map(lambda j: j[1], filter(lambda i: i[0] == opponent, tab)))
        return calculate_result((opponent, {
            "X": get_pair(losing_pairs),
            "Y": get_pair(ties),
            "Z": get_pair(winning_pairs)
        }[result]))


    with codecs.open("input.txt") as input_file:
        games = list(map(lambda line: tuple(line.strip().split(" ")), input_file.readlines()))
        results = sum(list(map(calculate_result, games)))
        print("part 1:", results)
        results = sum(list(map(play_2, games)))
        print("part 2:", results)
