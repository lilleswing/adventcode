from aoc2019 import read_file

def myf(x):
    return x // 3 - 2


def myf2(x):
    total =0
    gas = x // 3 - 2
    while gas != 0:
        total += gas
        gas = gas // 3 - 2
        if gas < 0:
            gas = 0
    return total


def solve1():
    pinput = read_file('1.txt')
    pinput = [int(x) for x in pinput]
    return sum([myf(x) for x in pinput])


def solve2():
    pinput = read_file('1.txt')
    pinput = [int(x) for x in pinput]
    return sum([myf2(x) for x in pinput])

def test_solve1():
    assert solve1() == 3452245

def test_solve2():
    assert solve2() == 5175499
