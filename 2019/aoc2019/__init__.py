from typing import List
import os
from collections import defaultdict

ASSET_FOLDER = os.path.join(os.path.dirname(__file__), 'data')


def read_file(fname):
    fname = os.path.join(ASSET_FOLDER, fname)
    with open(fname) as fin:
        return [x.strip() for x in fin.readlines()]


class Computer(object):
    ADD_OP_CODE = 1
    MULTIPLY_OP_CODE = 2
    INPUT_OP_CODE = 3
    OUTPUT_OP_CODE = 4
    JIT_OP_CODE = 5
    JIF_OP_CODE = 6
    LT_OP_CODE = 7
    EQ_OP_CODE = 8
    REL_BASE_CODE = 9
    HALT_OP_CODE = 99

    POSITION_MODE = 0
    IMMEDIATE_MODE = 1
    RELATIVE_MODE = 2

    def __init__(self, l: List[int], my_input: List[int] = None):
        """
        :param l: list of instructions for computer
        :param my_input: list of int
        """
        if my_input is None:
            my_input = []
        self.index = 0
        self.l = defaultdict(int)
        for i, elem in enumerate(l):
            self.l[i] = elem
        self.complete = False
        self.input = my_input
        self.relative_base = 0
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
        if mode == Computer.RELATIVE_MODE:
            return self.l[value + self.relative_base]
        return value

    def get_dest_index(self, index, op_code):
        dest_index = self.get_register(index)
        if op_code == Computer.RELATIVE_MODE:
            return dest_index + self.relative_base
        return dest_index

    def get_register(self, index, op_code=None):
        if op_code is None:
            return self.l[index]
        if op_code == Computer.RELATIVE_MODE:
            return self.l[index] + self.relative_base
        return self.l[index]

    def _add(self, op_code):
        v1 = self.get_variable(self.get_register(self.index + 1), op_code[0])
        v2 = self.get_variable(self.get_register(self.index + 2), op_code[1])
        result = v1 + v2
        dest_index = self.get_register(self.index + 3, op_code[2])
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
        dest_index = self.get_register(self.index + 3, op_code[2])
        if v1 < v2:
            self.l[dest_index] = 1
        else:
            self.l[dest_index] = 0
        self.index += 4

    def _eq(self, op_code):
        v1 = self.get_variable(self.get_register(self.index + 1), op_code[0])
        v2 = self.get_variable(self.get_register(self.index + 2), op_code[1])
        dest_index = self.get_register(self.index + 3, op_code[2])
        if v1 == v2:
            self.l[dest_index] = 1
        else:
            self.l[dest_index] = 0
        self.index += 4

    def _multiply(self, op_code):
        v1 = self.get_variable(self.get_register(self.index + 1), op_code[0])
        v2 = self.get_variable(self.get_register(self.index + 2), op_code[1])
        result = v1 * v2
        dest_index = self.get_register(self.index + 3, op_code[2])
        self.l[dest_index] = result
        self.index += 4

    def _halt(self):
        self.complete = True

    def _input(self, op_code):
        if self.input is None or len(self.input) == 0:
            raise ValueError("Attempted Input without Setting One From user")
        v1 = self.get_register(self.index + 1, op_code[0])
        self.l[v1] = self.input[0]
        self.input = self.input[1:]
        self.index += 2

    def _output(self, op_code):
        v1 = self.get_variable(self.get_register(self.index + 1), op_code[0])
        self.outputs.append(v1)
        self.index += 2

    def _adj_relative_base(self, op_code):
        v1 = self.get_variable(self.get_register(self.index + 1), op_code[0])
        self.relative_base += v1
        self.index += 2

    def _run_step(self):
        switch_code = int(self.l[self.index]) % 100
        op_code = self._zero_pad(self.l[self.index], 10)
        if switch_code == Computer.HALT_OP_CODE:
            self._halt()
            return
        if switch_code == Computer.ADD_OP_CODE:
            self._add(op_code)
            return
        if switch_code == Computer.MULTIPLY_OP_CODE:
            self._multiply(op_code)
            return
        if switch_code == Computer.INPUT_OP_CODE:
            self._input(op_code)
            return
        if switch_code == Computer.OUTPUT_OP_CODE:
            self._output(op_code)
            return
        if switch_code == Computer.JIT_OP_CODE:
            self._jit(op_code)
            return
        if switch_code == Computer.JIF_OP_CODE:
            self._jif(op_code)
            return
        if switch_code == Computer.LT_OP_CODE:
            self._lt(op_code)
            return
        if switch_code == Computer.EQ_OP_CODE:
            self._eq(op_code)
            return
        if switch_code == Computer.REL_BASE_CODE:
            self._adj_relative_base(op_code)
            return
        raise ValueError()

    def run_to_completion(self):
        while not self.complete:
            self._run_step()
        return self.l[0]

    def run_until_output(self):
        num_outputs = len(self.outputs)
        while not self.complete and num_outputs == len(self.outputs):
            self._run_step()
