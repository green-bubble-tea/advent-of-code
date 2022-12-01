import codecs
import re
from itertools import combinations_with_replacement, permutations


def get_ints(string):
    return list(map(int, re.findall(r'-?\d+', string)))


def calculate_cookie_score_with_calories(spoons, ingredients_list):
    no_calories, calories = list(map(lambda i: i[:-1], ingredients_list)), list(
        map(lambda i: [i[-1]], ingredients_list))
    score = calculate_cookie_score(spoons, no_calories)
    calories = calculate_cookie_score(spoons, calories)
    return score, calories


def calculate_cookie_score(spoons, ingredients_list):
    score = 1
    for ingredient_index in range(len(ingredients_list[0])):
        tmp = 0
        for index, value in enumerate(spoons):
            tmp += value * ingredients_list[index][ingredient_index]
        if tmp < 0:
            return 0
        else:
            score *= tmp
    return score


def get_max_score(spoons_combination, ingredients_list, part2=False):
    max_score = 0
    ingredients_no_calories = list(map(lambda i: i[:-1], ingredients_list))
    for combination in spoons_combination:
        permutation = permutations(combination)
        for perm in permutation:
            if not part2:
                cookie_score = calculate_cookie_score(perm, ingredients_no_calories)
                if cookie_score > max_score:
                    max_score = cookie_score
            else:
                cookie_score, calories_count = calculate_cookie_score_with_calories(perm, ingredients_list)
                if cookie_score > max_score and calories_count == 500:
                    max_score = cookie_score
    return max_score


if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        ingredients = [get_ints(i) for i in input_file.readlines()]
        target, ingredients_count = 100, len(ingredients)
        spoons_combinations = list(
            filter(lambda i: sum(i) == target, combinations_with_replacement(range(1, target + 1), ingredients_count)))
        print("part 1:", get_max_score(spoons_combinations, ingredients))
        print("part 2:", get_max_score(spoons_combinations, ingredients, part2=True))
