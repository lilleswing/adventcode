from .day05 import solve1, solve2, day2_solve1, day2_solve2
from .day07 import amp_for_file, solve1 as d7solve1, solve2 as d7solve2


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
