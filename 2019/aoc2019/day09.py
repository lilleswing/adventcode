from aoc2019 import read_file, Computer


def solve1():
    l = read_file('day9.in')
    l = [int(x) for x in l[0].split(',')]

    c = Computer(l, [1])
    c.run_to_completion()
    return c.outputs[-1]


def solve2():
    l = read_file('day9.in')
    l = [int(x) for x in l[0].split(',')]

    c = Computer(l, [2])
    c.run_to_completion()
    return c.outputs[-1]
