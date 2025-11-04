import itertools
import numpy as np

def mix(a, b):
    return a ^ b

def prune(a):
    return a % 16777216
def next_num(n):
    m = mix(n, n * 64)
    m = prune(m)
    m = mix(m, m // 32)
    m = prune(m)
    m = mix(m, m * 2048)
    m = prune(m)
    return m

def part1():
    data = [int(x) for x in open('day22.sample').readlines()]
    retval = []
    for n in data:
        for i in range(2000):
            n = next_num(n)
        retval.append(n)
    print(sum(retval))

def get_rollouts():
    data = [int(x) for x in open('day22.in').readlines()]
    retval = []
    combo = []
    for n in data:
        row = {}
        ones = n % 10
        for i in range(2000):
            n = next_num(n)
            next_one = n % 10
            combo.append(next_one - ones)
            if len(combo) > 4:
                combo = combo[-4:]
            key = tuple(combo)
            if key not in row:
                row[key] = next_one
            ones = next_one
        retval.append(row)
    return retval


def match_combo(rollout, combo):
    key = tuple(combo)
    if key not in rollout:
        return None
    return rollout[key]

def get_total_price(rollouts, combo):
    total = 0
    for rollout in rollouts:
        r = match_combo(rollout, combo)
        if r is not None:
            total += r
    return total

def part2():
    """
    :return: 
    """
    possible_values = range(-9, 10)
    all_combinations = itertools.product(possible_values, repeat=4)
    rollouts = get_rollouts()

    best_price = 0
    for combo in all_combinations:
        total_price = get_total_price(rollouts, combo)
        if total_price > best_price:
            best_price = total_price
            print(combo, total_price)

if __name__ == "__main__":
    part1()
    part2()
