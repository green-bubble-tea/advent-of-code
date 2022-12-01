from collections import Counter

password = "hxbxwxba"


def overlapping(s):
    t = [(i, j, k) for i, j, k in zip(s, s[1:], s[2:]) if i == j and j == k]
    return len(t) != 0


def no_forbidden_letters(s):
    return all(i not in s for i in list("iol"))


def has_pairs(s):
    t = Counter([(i, j) for i, j in zip(s, s[1:]) if i == j])
    return len(t) > 1 and not overlapping(s)


def has_consecutive_letters(s):
    t = [(i, j, k) for i, j, k in zip(s, s[1:], s[2:]) if ord(i) == ord(j) - 1 and ord(j) == ord(k) - 1]
    return len(t) != 0


def next_letter(s):
    return chr(ord(s) + 1) if s != "z" else "a"


def increase_password(s):
    stopped = False
    new_str = []
    index = len(s) - 1
    while not stopped:
        current_letter = s[index]
        next_ = next_letter(current_letter)
        new_str.insert(0, next_)
        if next_ != "a":
            stopped = True
        else:
            index -= 1
    return f"{s[:index]}{''.join(new_str)}"


def is_ok(s):
    return has_pairs(s) and no_forbidden_letters(s) and has_consecutive_letters(s)


if __name__ == "__main__":
    while not is_ok(password):
        password = increase_password(password)
    print("part 1:", password)
    password = increase_password(password)
    if is_ok(password):
        print("part 2:", password)
    else:
        while not is_ok(password):
            password = increase_password(password)
        print("part 2:", password)
