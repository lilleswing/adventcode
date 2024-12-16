import numpy as np


def expand(a):
    """
    :param lines:
    :return:
    if any row or column in 'a' has only '.' then add another row or column
    """
    to_add_rows = []
    for r in range(a.shape[0]):
        if np.all(a[r] == '.'):
            to_add_rows.append(r)
    for v in to_add_rows[::-1]:
        a = np.insert(a, v, '.', axis=0)
    to_add_cols = []
    for c in range(a.shape[1]):
        if np.all(a[:, c] == '.'):
            to_add_cols.append(c)
    for v in to_add_cols[::-1]:
        a = np.insert(a, v, '.', axis=1)
    return a


def part1(fname):
    lines = [x.strip() for x in open(fname).readlines()]
    lines = [list(x) for x in lines]
    lines = np.array(lines)
    board = expand(lines)

    galaxies = np.where(board == '#')
    galaxies = list(zip(galaxies[0], galaxies[1]))
    total = 0
    for g1 in galaxies:
        for g2 in galaxies:
            if g1 == g2:
                continue
            total += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    print(total / 2)


def expand2(a):
    """
    :param lines:
    :return:
    if any row or column in 'a' has only '.' then add another row or column
    """
    to_add_rows = []
    for r in range(a.shape[0]):
        if np.all(a[r] == '.'):
            to_add_rows.append(r)
    to_add_cols = []
    for c in range(a.shape[1]):
        if np.all(a[:, c] == '.'):
            to_add_cols.append(c)
    return to_add_rows, to_add_cols


def part2(fname):
    if fname == 'day11.sample':
        expansion_size = 100
    else:
        expansion_size = 1_000_000
    lines = [x.strip() for x in open(fname).readlines()]
    lines = [list(x) for x in lines]
    lines = np.array(lines)
    board = lines
    to_add_rows, to_add_cols = expand2(lines)
    def count_wormhols(l, g1, g2):
        g1, g2 = sorted([g1, g2])
        count = 0
        for v in l:
            if g1 < v < g2:
                count += 1
        return count
    galaxies = np.where(board == '#')
    galaxies = list(zip(galaxies[0], galaxies[1]))
    total = 0
    for g1 in galaxies:
        for g2 in galaxies:
            if g1 == g2:
                continue
            # count number of to_add_rows
            num_row_hop = count_wormhols(to_add_rows, g1[0], g2[0])
            num_col_hop = count_wormhols(to_add_cols, g1[1], g2[1])
            total += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
            total += num_row_hop * (expansion_size-1)
            total += num_col_hop * (expansion_size-1)
    print(total / 2)


if __name__ == "__main__":
    # part1('day11.in')
    part2('day11.in')
