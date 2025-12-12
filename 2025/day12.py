import re
from functools import lru_cache

"""
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""

def parse_present(lines):
    lines = lines[1:]
    grid = []
    while lines[0] != "":
        grid.append(lines[0])
        lines = lines[1:]
    lines = lines[1:]
    return tuple(grid), lines


def parse_requirement(lines):
    p1, p2 = lines[0].split(': ')
    dims = tuple(map(int, p1.split('x')))
    present_reqs = [int(x) for x in p2.split(' ')]
    lines = lines[1:]
    return (dims, present_reqs), lines

def parse(lines):
    presents = []
    requirements = []
    while len(lines) > 0:
        line = lines[0]
        if line.find('x') != -1:
            requirement, lines = parse_requirement(lines)
            requirements.append(requirement)
        else:
            present, lines = parse_present(lines)
            presents.append(present)
    return presents, requirements

def ez_fit(requirement):
    fx, fy = requirement[0]
    presents = requirement[1]
    block_x = fx // 3
    block_y = fy // 3
    total_blocks =  block_x * block_y
    return sum(presents) < total_blocks

@lru_cache(maxsize=None)
def count_squares(p):
    total = 0
    for r in p:
        for c in r:
            if c == '#':
                total += 1
    return total


def can_fit(requirement, presents):
    fx, fy = requirement[0]
    need_p = requirement[1]
    sq_to_fill = 0
    for idx, p in enumerate(need_p):
        sq_to_fill += (count_squares(presents[idx]) * p)
    return sq_to_fill < fx * fy



def part1():
    data = [x.strip() for x in open('day12.in').readlines()]
    presents, requirements = parse(data)

    print(f"N Requirements: {len(requirements)}")
    total = 0
    for r in requirements:
        if can_fit(r, presents):
            total += 1
    print(f"Solutions: {total}")


    pass

if __name__ == "__main__":
    part1()