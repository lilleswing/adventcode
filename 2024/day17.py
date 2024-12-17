import re


class Computer(object):
    def __init__(self, a, b, c, program):
        self.a = a
        self.b = b
        self.c = c
        self.program = program
        self.instruction_pointer = 0
        self.out_buffer = []
        self.inst_lookup = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv
        }

    def get_combo_value(self, opcode):
        if opcode == 4:
            return self.a
        if opcode == 5:
            return self.b
        if opcode == 6:
            return self.c
        if opcode == 7:
            raise ValueError("Opcode 7 combo value")
        return opcode

    def adv(self, v):
        v = self.get_combo_value(v)
        v = 2 ** v
        retval = self.a // v
        self.a = retval
        self.instruction_pointer += 2

    def bxl(self, v):
        self.b = self.b ^ v
        self.instruction_pointer += 2

    def bst(self, v):
        v = self.get_combo_value(v)
        v %= 8
        self.b = v
        self.instruction_pointer += 2

    def jnz(self, v):
        if self.a == 0:
            self.instruction_pointer += 2
            return
        self.instruction_pointer = v

    def bxc(self, v):
        self.b = self.b ^ self.c
        self.instruction_pointer += 2

    def out(self, v):
        v = self.get_combo_value(v)
        v %= 8
        self.out_buffer.append(v)
        self.instruction_pointer += 2

    def bdv(self, v):
        v = self.get_combo_value(v)
        v = 2 ** v
        retval = self.a // v
        self.b = retval
        self.instruction_pointer += 2

    def cdv(self, v):
        v = self.get_combo_value(v)
        v = 2 ** v
        retval = self.a // v
        self.c = retval
        self.instruction_pointer += 2

    def move_step(self):
        if self.instruction_pointer + 1 >= len(self.program):
            return False
        inst = self.program[self.instruction_pointer]
        opcode = self.program[self.instruction_pointer + 1]
        self.inst_lookup[inst](opcode)
        return True

    def run_program(self):
        steps = 0
        is_alive = True
        while is_alive:
            try:
                is_alive = self.move_step()
                steps += 1
            except Exception as e:
                print(f"Failed on step {steps}")
                raise e

    def __str__(self):
        return f"a: {self.a}, b: {self.b}, c: {self.c}, ip: {self.instruction_pointer}, out: {self.out_buffer}, program: {self.program}"


def parse(fname):
    lines = [x.strip() for x in open(fname).readlines()]
    a = re.findall(r"\d+", lines[0])[0]
    b = re.findall(r"\d+", lines[1])[0]
    c = re.findall(r"\d+", lines[2])[0]

    program = lines[4].replace("Program: ", "").split(",")
    program = [int(x) for x in program]
    return Computer(int(a), int(b), int(c), program)


def part1(fname):
    computer = parse(fname)
    print(computer)
    computer.run_program()
    print(computer)
    print(",".join([str(x) for x in computer.out_buffer]))


def dfs(program, a_reg_bin, need_idx):
    if need_idx == len(program):
        return True
    program_digit = len(program) - need_idx - 1
    a_reg_digits = need_idx * 3, need_idx * 3 + 1, need_idx * 3 + 2
    for i in range(8):
        a_reg_bin[a_reg_digits[2]] = i & 1
        a_reg_bin[a_reg_digits[1]] = (i >> 1) & 1
        a_reg_bin[a_reg_digits[0]] = (i >> 2) & 1
        a_reg = int("".join([str(x) for x in a_reg_bin]), 2)
        computer = Computer(a_reg, 0, 0, program)
        computer.run_program()
        if len(computer.out_buffer) != len(program):
            continue
        if program[program_digit] == computer.out_buffer[program_digit]:
            if dfs(program, a_reg_bin, need_idx + 1):
                return True
    return False


def part2(fname):
    computer = parse(fname)
    program = computer.program
    a_reg_bin = [0] * (len(program) * 3)
    retval = dfs(program, a_reg_bin, 0)
    if not retval:
        raise ValueError("Failed to find solution")
    a_reg = int("".join([str(x) for x in a_reg_bin]), 2)
    print(f"Solution: {a_reg}")
    c = Computer(a_reg, 0, 0, program)
    c.run_program()
    print(program)
    print(c.out_buffer)


if __name__ == "__main__":
    # part1('day17.in')
    part2('day17.in')
