import codecs

if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        lines = list(map(str.strip, input_file.readlines()))
        cycle_no = 1
        index = 0
        register = 1
        cycle_skip = False
        cycles = [20, 60, 100, 140, 180, 220]
        signal_strengths = 0
        calculate_sprite_position = lambda i: (i - 1, i, i + 1)
        sprite_position = calculate_sprite_position(register)
        pixel = 0
        screen = ""
        while index < len(lines):
            current_instruction = lines[index]
            sprite_position = calculate_sprite_position(register)
            if pixel in sprite_position:
                screen += "#"
            else:
                screen += "."
            pixel += 1
            if cycle_no % 40 == 0:
                screen += "\n"
                pixel = 0
            if cycle_no in cycles:
                signal_strengths += cycle_no * register
            if current_instruction == "noop":
                cycle_no += 1
                index += 1
            else:
                value = int(current_instruction.split(" ")[-1])
                if not cycle_skip:
                    cycle_skip = True
                    cycle_no += 1
                else:
                    cycle_skip = False
                    cycle_no += 1
                    index += 1
                    register += value
        print("part 1:", signal_strengths)
        print("part 2:")
        print(screen)
