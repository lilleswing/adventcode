import itertools
from collections import defaultdict

import tqdm


def generate_bitstrings(n, k):
    """Generates all bitstrings of length n with a sum of k.

    Args:
      n: The length of the bitstring.
      k: The desired sum of the bits.

    Yields:
      A generator of bitstrings.
    """

    for combination in itertools.combinations(range(n), k):
        bitstring = ['.'] * n
        for i in combination:
            bitstring[i] = '#'
        yield ''.join(bitstring)


def replace_bitstring(s, replacements):
    retval = ""
    replacement_idx = 0
    for i, c in enumerate(s):
        if c == '?':
            retval += replacements[replacement_idx]
            replacement_idx += 1
        else:
            retval += c
    return retval


def check_bitstring(s, vs):
    my_count = 0
    counts = []
    for i, c in enumerate(s):
        if c == '.':
            if my_count != 0:
                counts.append(my_count)
            my_count = 0
        if c == '#':
            my_count += 1
    if my_count != 0:
        counts.append(my_count)
    return counts == vs


def solve_line(line):
    line = line.split(' ')
    n = line[0].count('?')
    vs = [int(x) for x in line[1].split(',')]
    k = sum(vs) - line[0].count('#')

    total = 0
    for bitstring in generate_bitstrings(n, k):
        my_v = replace_bitstring(line[0], bitstring)
        if check_bitstring(my_v, vs):
            total += 1
    return total


def part1(fname):
    lines = open(fname).readlines()
    lines = [x.strip() for x in lines]
    total = 0
    for line in tqdm.tqdm(lines):
        # v = solve_line(line)
        total += solve_line(line)
    print(total)


def solve_line2(line):
    line = line.split(' ')
    repeats = 5
    line[0] = "?".join([line[0]] * repeats) + "."
    line[1] = ",".join([line[1]] * repeats)
    goal_pattern = [int(x) for x in line[1].split(',')] + [0]
    solutions = defaultdict(int)
    solutions[(0,)] = 1
    for c in line[0]:
        new_solutions = defaultdict(int)
        for k, v in solutions.items():
            if c in ('#', '?'):
                new_solution = list(k)
                new_solution[-1] += 1
                new_solutions[tuple(new_solution)] += v
            if c in (".", '?'):
                new_solution = list(k)
                if new_solution[-1] != 0:
                    sol_len = len(new_solution)
                    if new_solution != goal_pattern[:sol_len]:
                        continue
                    new_solution.append(0)
                new_solutions[tuple(new_solution)] += v
        solutions = new_solutions
    # print(solutions)
    return solutions[tuple(goal_pattern)]


def part2(fname):
    lines = open(fname).readlines()
    lines = [x.strip() for x in lines]
    total = 0
    for line in tqdm.tqdm(lines):
        v = solve_line2(line)
        total += v
    print(total)


if __name__ == "__main__":
    # part1('day12.in')
    part2('day12.in')
