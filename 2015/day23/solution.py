import codecs

if __name__ == "__main__":
    def inc(register):
        return registers[register] + 1


    def hlf(register):
        return registers[register] / 2


    def tpl(register):
        return registers[register] * 3


    def jmp(index, value):
        return index + value


    def jie(index, value, register):
        if registers[register] % 2 == 0:
            return index + value
        else:
            return index + 1


    def jio(index, value, register):
        if registers[register] == 1:
            return index + value
        else:
            return index + 1


    def execute(instructions):
        offset = 0
        while offset < len(instructions):
            line = instructions[offset]
            instruction, *rest = line
            if instruction in ["inc", "hlf", "tpl"]:
                register_value = "".join(rest)
                result = globals()[instruction](register_value)
                registers[register_value] = result
                offset += 1
            elif instruction == "jmp":
                offset = jmp(offset, int("".join(rest)))
            else:
                register_value, jump = rest
                jump = int(jump)
                offset = globals()[instruction](offset, jump, register_value)


    with codecs.open("input.txt") as input_file:
        lines = list(map(lambda i: i.strip().replace(",", "").split(" "), input_file.readlines()))
        registers = dict(a=0, b=0)
        execute(lines)
        print("part 1:", registers.get("b"))
        registers = dict(a=1, b=0)
        execute(lines)
        print("part 2:", registers.get("b"))
