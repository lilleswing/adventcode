from aoc2019 import read_file


class Computer(object):
    ADD_OP_CODE = 1
    MULTIPLY_OP_CODE = 2
    INPUT_OP_CODE = 3
    OUTPUT_OP_CODE = 4
    JIT_OP_CODE = 5
    JIF_OP_CODE = 6
    LT_OP_CODE = 7
    EQ_OP_CODE = 8
    HALT_OP_CODE = 99

    POSITION_MODE = 0
    IMMEDIATE_MODE = 1

    def __init__(self, l, my_input=None):
        self.index = 0
        self.l = l
        self.complete = False
        self.input = my_input
        self.outputs = []

    def _zero_pad(self, i, op_numbers):
        """
        return 0 padded op code to account for all the ops
        """
        length = op_numbers + 2
        s = str(i)
        while len(s) < length:
            s = "0" + s
        l = [int(x) for x in s]
        modes = l[:-2]
        return modes[::-1]

    def get_variable(self, value, mode):
        if mode == Computer.POSITION_MODE:
            return self.l[value]
        return value

    def get_register(self, index):
        return self.l[index]

    def _add(self, op_code):
        v1 = self.get_variable(self.get_register(self.index + 1), op_code[0])
        v2 = self.get_variable(self.get_register(self.index + 2), op_code[1])
        result = v1 + v2
        dest_index = self.get_register(self.index + 3)
        self.l[dest_index] = result
        self.index += 4

    def _jit(self, op_code):
        v1 = self.get_variable(self.get_register(self.index + 1), op_code[0])
        v2 = self.get_variable(self.get_register(self.index + 2), op_code[1])
        if v1 != 0:
            self.index = v2
        else:
            self.index += 3

    def _jif(self, op_code):
        v1 = self.get_variable(self.get_register(self.index + 1), op_code[0])
        v2 = self.get_variable(self.get_register(self.index + 2), op_code[1])
        if v1 == 0:
            self.index = v2
        else:
            self.index += 3

    def _lt(self, op_code):
        v1 = self.get_variable(self.get_register(self.index + 1), op_code[0])
        v2 = self.get_variable(self.get_register(self.index + 2), op_code[1])
        dest_index = self.get_register(self.index + 3)
        if v1 < v2:
            self.l[dest_index] = 1
        else:
            self.l[dest_index] = 0
        self.index += 4

    def _eq(self, op_code):
        v1 = self.get_variable(self.get_register(self.index + 1), op_code[0])
        v2 = self.get_variable(self.get_register(self.index + 2), op_code[1])
        dest_index = self.get_register(self.index + 3)
        if v1 == v2:
            self.l[dest_index] = 1
        else:
            self.l[dest_index] = 0
        self.index += 4

    def _multiply(self, op_code):
        v1 = self.get_variable(self.get_register(self.index + 1), op_code[0])
        v2 = self.get_variable(self.get_register(self.index + 2), op_code[1])
        result = v1 * v2
        dest_index = self.get_register(self.index + 3)
        self.l[dest_index] = result
        self.index += 4

    def _halt(self):
        self.complete = True

    def _input(self, op_code):
        if self.input is None:
            raise ValueError("Attempted Input without Setting One From user")
        v1 = self.get_register(self.index + 1)
        self.l[v1] = self.input
        self.index += 2

    def _output(self, op_code):
        v1 = self.get_variable(self.get_register(self.index + 1), op_code[0])
        self.outputs.append(v1)
        self.index += 2

    def run_to_completion(self):
        while not self.complete:
            switch_code = int(self.l[self.index]) % 100
            op_code = self._zero_pad(self.l[self.index], 10)
            print(self.index, switch_code)
            if switch_code == Computer.HALT_OP_CODE:
                self._halt()
                continue
            if switch_code == Computer.ADD_OP_CODE:
                self._add(op_code)
                continue
            if switch_code == Computer.MULTIPLY_OP_CODE:
                self._multiply(op_code)
                continue
            if switch_code == Computer.INPUT_OP_CODE:
                self._input(op_code)
                continue
            if switch_code == Computer.OUTPUT_OP_CODE:
                self._output(op_code)
                continue
            if switch_code == Computer.JIT_OP_CODE:
                self._jit(op_code)
                continue
            if switch_code == Computer.JIF_OP_CODE:
                self._jif(op_code)
                continue
            if switch_code == Computer.LT_OP_CODE:
                self._lt(op_code)
                continue
            if switch_code == Computer.EQ_OP_CODE:
                self._eq(op_code)
                continue
            raise ValueError()

        return self.l[0]


def parse_input_day2():
    # return [1,0,0,0, 99]
    # return [2,3,0,3,99]
    # return [2, 4, 4, 5, 99, 0]
    l = read_file('day2.in')
    l = [int(x) for x in l[0].split(',')]
    l[1] = 12
    l[2] = 2
    return l


def parse_input_day5():
    # return [1,0,0,0, 99]
    # return [2,3,0,3,99]
    # return [2, 4, 4, 5, 99, 0]
    l = read_file('day5.in')
    l = [int(x) for x in l[0].split(',')]
    return l


def day2_solve1():
    l = parse_input_day2()
    computer = Computer(l)
    return computer.run_to_completion()


def run_round(noun, verb):
    l = parse_input_day2()
    l[1] = noun
    l[2] = verb
    computer = Computer(l)
    return computer.run_to_completion()


def solve2_helper(goal):
    for i in range(0, 101):
        for j in range(0, 101):
            if run_round(i, j) == goal:
                return 100 * i + j


def day2_solve2():
    goal = 19690720
    return solve2_helper(goal)


def test_day2_solve1():
    assert day2_solve1() == 9581917


def test_day2_solve2():
    assert day2_solve2() == 2505


def solve1():
    l = parse_input_day5()
    computer = Computer(l, 1)
    computer.run_to_completion()
    return computer.outputs[-1]


def solve2():
    l = parse_input_day5()
    computer = Computer(l, 5)
    computer.run_to_completion()
    return computer.outputs[-1]


def test_solve1():
    assert solve1() == 6745903


def test_solve2():
    assert solve2() == 9168267
