import numpy as np


def solve1(line):
    if np.all(line == 0):
        return 0
    deltas = []
    for i in range(1, len(line)):
        deltas.append(line[i] - line[i - 1])
    deltas = np.array(deltas)
    next_row_val = solve1(deltas)
    return line[-1] + next_row_val


def part1(fname):
    lines = open(fname).readlines()
    lines = [list(x.strip().split()) for x in lines]
    total = 0
    for line in lines:
        line = [int(x) for x in line]
        line = np.array(line)
        v = solve1(line)
        total += v
    print(total)

def solve2(line):
    if np.all(line == 0):
        return 0
    deltas = []
    for i in range(1, len(line)):
        deltas.append(line[i] - line[i - 1])
    deltas = np.array(deltas)
    next_row_val = solve2(deltas)
    return line[0] - next_row_val

def part2(fname):
    lines = open(fname).readlines()
    lines = [list(x.strip().split()) for x in lines]
    total = 0
    for line in lines:
        line = [int(x) for x in line]
        line = np.array(line)
        v = solve2(line)
        total += v
    print(total)


if __name__ == "__main__":
    # part1('day09.in')
    part2('day09.in')
