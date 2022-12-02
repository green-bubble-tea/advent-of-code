NUMBER = 34000000
max_ = 1000001


def find_house(part2=False):
    elf = 1
    found = False
    house_number = 0
    houses = [0 for _ in range(1, max_)]
    while not found and elf < max_:
        if not part2:
            for i in range(elf, max_ - 1, elf):
                houses[i] += 10 * elf
                if houses[i] >= NUMBER:
                    house_number = i
                    found = True
            elf += 1
        else:
            current_house, delivery_no = elf, 1
            while current_house < max_ - 1 and delivery_no < 51:
                houses[current_house] += 11 * elf
                if houses[current_house] >= NUMBER:
                    found = True
                    house_number = current_house
                current_house += elf
                delivery_no += 1
            elf += 1
    return house_number


if __name__ == "__main__":
    print("part 1:", find_house())
    print("part 2:", find_house(part2=True))
