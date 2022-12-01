import hashlib

input_string = "bgvyzdsv"


def find_hash(pattern):
    candidate = 0
    while True:
        string = f"{input_string}{candidate}"
        candidate_hash = hashlib.md5(string.encode("ascii")).hexdigest()
        if candidate_hash.startswith(pattern):
            return candidate
        candidate += 1


if __name__ == "__main__":
    desired_hash_part1, desired_hash_part2 = "0" * 5, "0" * 6
    print("part 1:", find_hash(desired_hash_part1))
    print("part 2:", find_hash(desired_hash_part2))
