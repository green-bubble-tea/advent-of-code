number = str(3113322113)


def split_number(s):
    number_list = []
    current_group = s[0]
    for char in range(1, len(s)):
        if s[char] == s[char - 1]:
            current_group += s[char]
        else:
            number_list.append(current_group)
            current_group = s[char]
        if char == len(s) - 1:
            number_list.append(current_group)
    return number_list


analyze_number = lambda s: "".join([f"{len(i)}{i[0]}" for i in s])


if __name__ == "__main__":
    for i in range(0, 50):
        number = analyze_number(split_number(number))
        if i == 39:
            print("part 1:", len(number))
    print("part 2:", len(number))
