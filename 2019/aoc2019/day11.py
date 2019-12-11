from aoc2019 import read_file, Computer
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

DIRECTIONS = {
    "NORTH": (-1, 0),
    "EAST": (0, 1),
    "SOUTH": (1, 0),
    "WEST": (0, -1)
}

DIRECTIONS_ORDERED = [
    "NORTH",
    "EAST",
    "SOUTH",
    "WEST"
]


def run_painting_program(starting_color=0):
    l = read_file('day11.in')[0]
    l = [int(x) for x in l.split(',')]

    paint = defaultdict(int)
    seen_locations = set()
    c = Computer(l)
    cur_loc = (0, 0)
    paint[cur_loc] = starting_color
    direction_index = 0  # NORTH
    while not c.complete:
        c.input.append(paint[cur_loc])
        c.run_until_output()
        c.run_until_output()
        if c.complete:
            break
        color, turn = c.outputs[-2:]
        paint[cur_loc] = color
        seen_locations.add(cur_loc)
        if turn == 1:
            direction_index += 1
        elif turn == 0:
            direction_index -= 1
        direction_index = (direction_index + len(DIRECTIONS_ORDERED)) % len(DIRECTIONS_ORDERED)

        my_english_direction = DIRECTIONS_ORDERED[direction_index]
        my_direction = DIRECTIONS[DIRECTIONS_ORDERED[direction_index]]
        cur_loc = cur_loc[0] + my_direction[0], cur_loc[1] + my_direction[1]

    return paint, seen_locations


def solve2():
    paint, seen_locations = run_painting_program(1)
    minr = min(seen_locations, key=lambda x: x[0])[0]
    maxr = max(seen_locations, key=lambda x: x[0])[0]
    minc = min(seen_locations, key=lambda x: x[1])[1]
    maxc = max(seen_locations, key=lambda x: x[1])[1]

    board = []
    for r in range(minr, maxr + 1):
        row = []
        for c in range(minc, maxc + 1):
            row.append(paint[(r, c)])
        board.append(row)
    a = np.array(board)
    print(a.shape)
    print(a)
    plt.imshow(a)
    plt.savefig('day11.png')


def solve1():
    paint, seen_locations = run_painting_program()
    print(len(seen_locations))
    return len(seen_locations)


def test_solve1():
    assert solve1() == 2088


if __name__ == "__main__":
    solve2()
