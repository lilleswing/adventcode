from typing import List

from aoc2019 import read_file
from . import Computer


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



def solve1():
    l = parse_input_day5()
    computer = Computer(l, [1])
    computer.run_to_completion()
    return computer.outputs[-1]


def solve2():
    l = parse_input_day5()
    computer = Computer(l, [5])
    computer.run_to_completion()
    return computer.outputs[-1]



