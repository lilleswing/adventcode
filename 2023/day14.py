import numpy as np

def bounds_check(lines, r, c):
    if r < 0 or r >= len(lines):
        return False
    if c < 0 or c >= len(lines[0]):
        return False
    return True


def roll_rock(lines, r, c):
    direction = (-1, 0)
    if lines[r][c] != 'O':
        return lines
    nr, nc = r + direction[0], c + direction[1]
    while bounds_check(lines, nr, nc):
        if lines[nr][nc] == '.':
            lines[r][c], lines[nr][nc] = lines[nr][nc], lines[r][c]
            r, c = nr, nc
            nr, nc = r + direction[0], c + direction[1]
        else:
            break
    return lines


def calculate_load(lines):
    total = 0
    for r in range(len(lines)):
        row_load = len(lines) - r
        for c in range(len(lines[0])):
            if lines[r][c] == 'O':
                total += row_load
    return total


def part1(fname):
    lines = open(fname).readlines()
    lines = [list(x.strip()) for x in lines]
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            lines = roll_rock(lines, r, c)
    for line in lines:
        print("".join(line))
    load = calculate_load(lines)
    print(load)


def run_cycle(lines):
    lines = np.array(lines)
    for k in [0,1,2,3]:
        lines = np.rot90(lines, -k)
        for r in range(len(lines)):
            for c in range(len(lines[0])):
                lines = roll_rock(lines, r, c)
        lines = np.rot90(lines, k)
    return lines


def make_key(lines):
    r = "".join(["".join(x) for x in lines])
    return r

def print_lines(lines):
    for line in lines:
        print("".join(line))

def part2(fname):
    lines = open(fname).readlines()
    lines = [list(x.strip()) for x in lines]
    cache = {}
    cycle = 0
    key = None
    goal = 1_000_000_000
    while key not in cache:
        key = make_key(lines)
        cache[key] = cycle
        lines = run_cycle(lines)
        key = make_key(lines)
        cycle += 1
    cycle_len = cycle - cache[key]
    goal = (goal - cache[key]) % cycle_len
    print(f"Cycle len: {cycle_len}")
    print(f"Cycle offset: {cache[key]}")
    print(f"Goal: {goal}")
    for _ in range(goal):
        lines = run_cycle(lines)
    print(calculate_load(lines))


if __name__ == "__main__":
    # part1('day14.in')
    part2('day14.in')
