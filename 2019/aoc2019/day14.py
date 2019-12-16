from aoc2019 import read_file
from functools import lru_cache
import math


def parse_token(t):
    t = t.strip()
    t = t.split(' ')
    return int(t[0]), t[1]


def parse_line(l):
    l1, l2 = l.split('=>')
    l2 = parse_token(l2)

    l1 = l1.split(',')
    l1 = [parse_token(x) for x in l1]
    return l1, l2


def find_recipe(count, elem, ds):
    for row in ds:
        target = row[-1]
        if target[1] == elem:
            return row
    raise ValueError(elem)


class OreCoster(object):
    def __init__(self, ds):
        self.ds = ds

    def ore_cost(self, count, elem, leftovers):
        """
        return the number of ore to make count elems
        leftovers = {elem: count}
        """
        leftovers = dict(leftovers)
        if elem == 'ORE':
            return count, leftovers
        if elem in leftovers and leftovers[elem] > count:
            leftovers[elem] -= count
            return 0, leftovers

        if elem in leftovers and leftovers[elem] == count:
            del leftovers[elem]
            return 0, leftovers

        if elem in leftovers:
            count -= leftovers[elem]
            del leftovers[elem]

        recipe, min_target = find_recipe(count, elem, self.ds)
        if count == min_target[0] and elem == min_target[1]:
            total_cost = 0
            for ingredient in recipe:
                retval = self.ore_cost(ingredient[0], ingredient[1], leftovers)
                my_ore_cost, leftovers = retval
                total_cost += my_ore_cost
            return total_cost, leftovers

        total_ore = 0
        total_ore_cost = 0
        while total_ore < count:
            min_ore_cost, leftovers = self.ore_cost(min_target[0], min_target[1], leftovers)
            total_ore_cost += min_ore_cost
            total_ore += min_target[0]
        leftovers[elem] = total_ore - count
        if leftovers[elem] == 0:
            del leftovers[elem]
        return total_ore_cost, leftovers

    def ore_cost2(self, count, elem, leftovers):
        """
            return the number of ore to make count elems
            leftovers = {elem: count}
        """
        leftovers = dict(leftovers)
        if elem == 'ORE':
            return count, leftovers
        if elem in leftovers and leftovers[elem] > count:
            leftovers[elem] -= count
            return 0, leftovers

        if elem in leftovers and leftovers[elem] == count:
            del leftovers[elem]
            return 0, leftovers

        if elem in leftovers:
            count -= leftovers[elem]
            del leftovers[elem]

        recipe, min_target = find_recipe(count, elem, self.ds)
        num_to_make = math.ceil(count / min_target[0])
        total_cost = 0
        for ingredient in recipe:
            retval = self.ore_cost2(ingredient[0] * num_to_make, ingredient[1], leftovers)
            my_ore_cost, leftovers = retval
            total_cost += my_ore_cost

        self_leftovers = min_target[0] * num_to_make - count
        if self_leftovers > 0:
            leftovers[elem] = self_leftovers
        return total_cost, leftovers


def test_solve1_sample():
    l = read_file('day14.sample')

    ds = [parse_line(x) for x in l]
    oc = OreCoster(ds)
    fuel_cost, leftovers = oc.ore_cost2(1, 'FUEL', {})
    assert 165 == fuel_cost


def test_solve1_sample2():
    l = read_file('day14.sample2')

    ds = [parse_line(x) for x in l]
    oc = OreCoster(ds)
    fuel_cost, leftovers = oc.ore_cost2(1, 'FUEL', {})
    assert 31 == fuel_cost


def solve1():
    l = read_file('day14.in')

    ds = [parse_line(x) for x in l]
    oc = OreCoster(ds)
    fuel_cost, leftovers = oc.ore_cost2(1, 'FUEL', {})
    print(fuel_cost, leftovers)
    # print(oc.ore_cost(4, 'CA'))
    # print(oc.ore_cost(3, 'BC'))
    # print(oc.ore_cost(2, 'AB'))
    return fuel_cost


def solve2():
    l = read_file('day14.in')

    ds = [parse_line(x) for x in l]
    oc = OreCoster(ds)
    goal = 1_000_000_000_000
    low, high = 10, 1000000000
    while low + 1 < high:
        guess = (low + high) // 2
        fuel_cost, leftovers = oc.ore_cost2(guess, 'FUEL', {})
        if fuel_cost < goal:
            low = guess
        else:
            high = guess
    fuel_cost_low, leftovers = oc.ore_cost2(low, 'FUEL', {})
    fuel_cost_high, leftovers = oc.ore_cost2(high, 'FUEL', {})
    print(low, high)
    print(fuel_cost_low, fuel_cost_high)
    return low


def test_solve2():
    assert solve2() == 1184209


if __name__ == "__main__":
    solve2()
