import codecs

me = {
    "Hit Points": 100,
    "Damage": 0,
    "Armor": 0
}

shop = {  # (cost, damage, armor)
    "Weapons": [(8, 4, 0),
                (10, 5, 0),
                (25, 6, 0),
                (40, 7, 0),
                (74, 8, 0)
                ],
    "Armor": [(13, 0, 1),
              (31, 0, 2),
              (53, 0, 3),
              (75, 0, 4),
              (102, 0, 5),
              (0, 0, 0)
              ],
    "Rings": [(25, 1, 0),
              (50, 20, 0),
              (100, 3, 0),
              (20, 0, 1),
              (40, 0, 2),
              (80, 0, 3),
              (0, 0, 0),
              (0, 0, 0)
              ]
}


def simulate_game(my_dict, boss_dict, player=True):
    if player:
        loss = max(my_dict["Damage"] - boss_dict["Armor"], 1)
        boss_dict["Hit Points"] -= loss
        if boss_dict["Hit Points"] <= 0:
            return True
        else:
            return simulate_game(my_dict, boss_dict, player=False)
    else:
        loss = max(boss_dict["Damage"] - my_dict["Armor"], 1)
        my_dict["Hit Points"] -= loss
        if my_dict["Hit Points"] <= 0:
            return False
        else:
            return simulate_game(my_dict, boss_dict)


if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        lines = list(map(lambda i: i.strip().split(": "), input_file.readlines()))
        boss = {i[0]: int(i[1]) for i in lines}
        min_cost, min_win, max_cost = 1000000, 100, 0
        for weapon in shop["Weapons"]:
            for armor in shop["Armor"]:
                for index1, ring1 in enumerate(shop["Rings"]):
                    for index2, ring2 in enumerate(shop["Rings"]):
                        if index1 != index2:
                            me_copy, boss_copy = me.copy(), boss.copy()
                            weapon_cost, weapon_damage, weapon_armor = weapon
                            armor_cost, armor_damage, armor_armor = armor
                            c1, d1, a1 = ring1
                            c2, d2, a2 = ring2
                            total_cost = sum((weapon_cost, armor_cost, c1, c2))
                            total_damage = sum((weapon_damage, armor_damage, d1, d2))
                            total_armor = sum((weapon_armor, armor_armor, a1, a2))
                            me_copy["Damage"] = total_damage
                            me_copy["Armor"] = total_armor
                            result = simulate_game(me_copy, boss_copy)
                            if result:
                                min_cost = min(min_cost, total_cost)
                            else:
                                max_cost = max(total_cost, max_cost)
        print("part 1:", min_cost)
        print("part 2:", max_cost)
