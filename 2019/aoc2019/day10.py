import math
from aoc2019 import read_file

import numpy as np
import fractions


def positive_rads(a):
    """
    make all radians positive
    """
    return (a + 8 * np.pi) % (2 * np.pi)


def cart2pol(x, y):
    rho = np.sqrt(x ** 2 + y ** 2)
    phi = np.arctan2(x, y)
    phi = positive_rads(phi)
    return rho, phi


def get_angle(x, y):
    try:
        f1 = fractions.Fraction(x, y)
    except:
        f1 = None

    try:
        f2 = fractions.Fraction(y, x)
    except:
        f2 = None
    return x > 0, y > 0, f1, f2


def calc_seen(r, c, board):
    if board[r][c] != '#':
        return 0
    seen_angles = set()
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] != '#':
                continue
            if y == r and c == x:
                continue
            dx = c - x  # Not sure direction is correct
            dy = r - y  # Not sure direction is correct
            phi = get_angle(dx, dy)
            if phi not in seen_angles:
                seen_angles.add(phi)
    return len(seen_angles)


def solve1_for_file(fname):
    board = read_file(fname)
    board = [list(x) for x in board]

    max_seen = -1
    for r in range(len(board)):
        for c in range(len(board)):
            seen = calc_seen(r, c, board)
            if seen > max_seen:
                max_seen = seen
    return max_seen


def find_station(fname):
    board = read_file(fname)

    board = [list(x) for x in board]

    max_seen = -1
    station = None
    for r in range(len(board)):
        for c in range(len(board)):
            seen = calc_seen(r, c, board)
            if seen > max_seen:
                station = (r, c)
                max_seen = seen
    print("Station at (%s,%s)" % station)
    return station, board


def solve2(fname='day10.in'):
    station, board = find_station(fname)
    s_y, s_x = station

    ordered = {}
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] != '#':
                continue
            if s_y == r and c == s_x:
                continue
            dx = c - s_x
            dy = s_y - r
            angle = get_angle(dx, dy)  # DeDupe on exact angles
            if angle not in ordered:
                ordered[angle] = []
            rho, phi = cart2pol(dx, dy)
            ordered[angle].append((rho, phi, (r, c)))  # add approximate angles for sorting

    ordered_by_angle = []
    for k, v in ordered.items():
        # Internal Sort by Distance from Origin
        v = sorted(v, key=lambda x: x[0])
        ordered[k] = v
        ordered_by_angle.append(v)

    # Sort by Angle
    ordered_by_angle = sorted(ordered_by_angle, key=lambda x: x[0][1])

    ordered_destruction = []
    index = 0
    while len(ordered_destruction) < 200:
        index = index % len(ordered_by_angle)
        if len(ordered_by_angle[index]) == 0:
            index += 1
            continue
        next_up = ordered_by_angle[index][0]
        ordered_destruction.append(next_up)
        ordered_by_angle[index] = ordered_by_angle[index][1:]
        index += 1
    print(ordered_destruction[199])
    _, _, coords = ordered_destruction[-1]
    y, x = coords
    return x * 100 + y


def solve1():
    return solve1_for_file('day10.in')


def test_solve1():
    assert solve1() == 247


def test_solve2():
    assert solve2() == 1919


def test_solve2_sample3():
    assert solve2('day10.sample3') == 802


def test_solve1_sample2():
    assert solve1_for_file('day10.sample2') == 8


def test_solve1_sample():
    assert solve1_for_file('day10.sample') == 33


if __name__ == "__main__":
    print(solve2())
