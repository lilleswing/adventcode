class Instruction(object):
    def __init__(self, s):
        self.s = s.split(" ", 1)


class Mips(object):
    def __init__(self, instructions):
        self.instructions = instructions
        self.a = 0
        self.b = 0
        self.index = 0

    def move(self):
        """
        :return next index may be out of range
        """
        inst = self.instructions[self.index]
        if inst.s[0] == 'hlf':
            return self._hlf()
        elif inst.s[0] == 'tpl':
            return self._tpl()
        elif inst.s[0] == 'inc':
            return self._inc()
        elif inst.s[0] == 'jmp':
            return self._jmp()
        elif inst.s[0] == 'jie':
            return self._jie()
        elif inst.s[0] == 'jio':
            return self._jio()

    def is_done(self):
        if self.index < 0 or self.index >= len(self.instructions):
            return True
        return False

    def _hlf(self):
        inst = self.instructions[self.index]
        if inst.s[1] == 'a':
            self.a /= 2
        else:
            self.b /= 2
        self.index += 1
        return self.index

    def _tpl(self):
        inst = self.instructions[self.index]
        if inst.s[1] == 'a':
            self.a *= 3
        else:
            self.b *= 3
        self.index += 1
        return self.index

    def _inc(self):
        inst = self.instructions[self.index]
        if inst.s[1] == 'a':
            self.a += 1
        else:
            self.b += 1
        self.index += 1
        return self.index

    def _jmp(self):
        inst = self.instructions[self.index]
        offset = int(inst.s[1])
        self.index += offset
        return self.index

    def _jie(self):
        inst = self.instructions[self.index]
        reg, offset = inst.s[1].split(', ')
        offset = int(offset)
        if reg == 'a':
            reg_value = self.a
        else:
            reg_value = self.b
        if reg_value % 2 == 0:
            self.index += offset
        else:
            self.index += 1
        return self.index

    def _jio(self):
        inst = self.instructions[self.index]
        reg, offset = inst.s[1].split(', ')
        offset = int(offset)
        if reg == 'a':
            reg_value = self.a
        else:
            reg_value = self.b
        if reg_value == 1:
            self.index += offset
        else:
            self.index += 1
        return self.index


def parse(lines):
    lines = [x.strip() for x in lines]
    instructions = list()
    for line in lines:
        instruction = Instruction(line)
        instructions.append(instruction)
    return Mips(instructions)


def solve1():
    mips = parse(open('day23.in').readlines())
    while not mips.is_done():
        mips.move()
    return mips.b


def solve2():
    mips = parse(open('day23.in').readlines())
    mips.a = 1
    while not mips.is_done():
        mips.move()
    return mips.b


def main():
    print(solve1())
    print(solve2())


if __name__ == "__main__":
    main()
