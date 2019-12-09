from aoc2019 import Computer
from aoc2019.day05 import solve1, solve2, day2_solve1, day2_solve2
from aoc2019.day07 import amp_for_file, solve1 as d7solve1, solve2 as d7solve2
from aoc2019.day09 import solve1 as d9solve1, solve2 as d9solve2


def test_day_9_solve2():
    assert d9solve2() == 50158


def test_day_9_solve1():
    assert d9solve1() == 3013554615


def test_day_7_part2():
    assert d7solve2() == 58285150


def test_day_7_part1():
    assert d7solve1() == 255590


def test_day7_sample2():
    assert amp_for_file('day7.sample2') == 54321


def test_day7_sample3():
    assert amp_for_file('day7.sample3') == 65210


def test_day7_sample1():
    assert amp_for_file('day7.sample') == 43210


def test_solve1():
    assert solve1() == 6745903


def test_solve2():
    assert solve2() == 9168267


def test_day2_solve1():
    assert day2_solve1() == 9581917


def test_day2_solve2():
    assert day2_solve2() == 2505


def test_relative_1():
    l = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
    c = Computer(l)
    c.run_to_completion()
    output = c.outputs[-1]
    assert len(str(output)) == 16


def test_relative_2():
    BIG_NUM = 1125899906842624
    l = [104, BIG_NUM, 99]
    c = Computer(l)
    c.run_to_completion()
    output = c.outputs[-1]
    assert output == BIG_NUM


def test_quine():
    l = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    c = Computer(l)
    c.run_to_completion()
    for i, o in zip(c.outputs, l):
        assert i == o
