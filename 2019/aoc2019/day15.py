from aoc2019 import read_file, Computer
import random
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.shortest_paths.generic import shortest_path, all_shortest_paths
from networkx.algorithms.shortest_paths import all_pairs_shortest_path_length


def print_board(board):
    VALUE_MAP = {
        "0": 0,
        "*": 1,
        ".": 2,
        "#": 3,
        "!": 4,
    }
    locs = list(board.keys())

    xvals = [x[1] for x in locs]
    minx, maxx = min(xvals), max(xvals)

    yvals = [x[0] for x in locs]
    miny, maxy = min(yvals), max(yvals)
    print(min(yvals), max(yvals))

    output = []
    for r in range(miny, maxy + 1):
        row = []
        for c in range(minx, maxx + 1):
            if r == 0 and c == 0:
                row.append("0")
            elif (r, c) not in board:
                row.append('*')
            else:
                row.append(board[(r, c)])
        output.append(row)

    for row in output:
        print(row)

    num_board = []
    for row in output:
        row = [VALUE_MAP[x] for x in row]
        num_board.append(row)
    plt.imshow(num_board)
    plt.savefig("day15.png")
    return output


DIRECTIONS = {
    "NORTH": (-1, 0),
    "SOUTH": (1, 0),
    "WEST": (0, -1),
    "EAST": (0, 1)
}

DIRECTION_NUMBERS = {
    1: (-1, 0),
    2: (1, 0),
    3: (0, -1),
    4: (0, 1)
}


def get_goal_loc(loc, my_direction):
    my_direction = DIRECTION_NUMBERS[my_direction]
    return loc[0] + my_direction[0], loc[1] + my_direction[1]


def random_walk():
    l = read_file('day15.in')[0]
    l = [int(x) for x in l.split(',')]

    loc = (0, 0)
    c = Computer(l)
    board = {}
    for i in range(10000):
        my_direction = random.choice([1, 2, 3, 4])
        c.input.append(my_direction)
        c.run_until_output()
        if c.complete:
            break

        response = c.outputs[-1]
        goal_loc = get_goal_loc(loc, my_direction)
        if response == 0:  # WALL
            board[goal_loc] = '#'  # '
            continue
        if response == 1:  # ALL Clear
            board[goal_loc] = '.'
            loc = goal_loc
            pass
        if response == 2:  # We Done!
            board[goal_loc] = "!"
            break

    print_board(board)


# Always Go Right
# [SOUTH, EAST, NORTH, WE$T]

ATTEMPT_ORDER = [
    ("WEST", (0, -1), 3),
    ("SOUTH", (1, 0), 2),
    ("EAST", (0, 1), 4),
    ("NORTH", (-1, 0), 1),
]


def move(computer, my_direction, loc, board):
    my_direction = my_direction[2]
    computer.input.append(my_direction)
    computer.run_until_output()
    response = computer.outputs[-1]
    goal_loc = get_goal_loc(loc, my_direction)
    if response == 0:  # WALL
        board[goal_loc] = '#'  # '
        return "WALL", loc
    if response == 1:  # ALL Clear
        board[goal_loc] = '.'
        return "CLEAR", goal_loc
    if response == 2:  # We Done!
        board[goal_loc] = "!"
        return "OXYGEN", goal_loc
    raise ValueError("MOVE FAILED")


def add_edges(g, board, r, c):
    my_loc = (r, c)
    if my_loc not in board or board[my_loc] != '.':
        return

    for description, vector, _ in ATTEMPT_ORDER:
        nr, nc = r + vector[0], c + vector[1]
        if (nr, nc) in board and board[(nr, nc)] == '.':
            g.add_edge(my_loc, (nr, nc))


def build_graph(board):
    g = nx.Graph()

    locs = list(board.keys())
    xvals = [x[1] for x in locs]
    minx, maxx = min(xvals), max(xvals)

    yvals = [x[0] for x in locs]
    miny, maxy = min(yvals), max(yvals)

    for r in range(miny, maxy + 1):
        for c in range(minx, maxx + 1):
            add_edges(g, board, r, c)

    return g


def shortest_path_to_oxygen(g, dest):
    my_path = shortest_path(g, (0, 0), dest)
    print(len(my_path) - 1, my_path[1:])
    return len(my_path) - 1  # Edges not nodes


def all_paths_from_oxygen(g, dest):
    my_paths = dict(all_pairs_shortest_path_length(g))[dest]
    return max(my_paths.values())


def solve2():
    l = read_file('day15.in')[0]
    l = [int(x) for x in l.split(',')]

    loc = (0, 0)
    oxygen_loc = None
    c = Computer(l)
    board = {}
    direction_index = 0
    for i in range(10000):
        my_direction = ATTEMPT_ORDER[direction_index]
        result, loc = move(c, my_direction, loc, board)
        if result == "WALL":
            direction_index = (direction_index + 4 + 1) % 4
        if result == "CLEAR":
            direction_index = (direction_index + 4 - 1) % 4
        if result == 'OXYGEN':
            direction_index = (direction_index + 4 - 1) % 4
            oxygen_loc = loc
            direction_index = (direction_index + 4 - 1) % 4

    print_board(board)
    board[oxygen_loc] = '.'
    board[(0, 0)] = '.'
    g = build_graph(board)
    max_length = all_paths_from_oxygen(g, oxygen_loc)
    print(max_length)
    return max_length


def solve1():
    l = read_file('day15.in')[0]
    l = [int(x) for x in l.split(',')]

    loc = (0, 0)
    c = Computer(l)
    board = {}
    direction_index = 0
    for i in range(100000):
        my_direction = ATTEMPT_ORDER[direction_index]
        result, loc = move(c, my_direction, loc, board)
        if result == "WALL":
            direction_index = (direction_index + 4 + 1) % 4
        if result == "CLEAR":
            direction_index = (direction_index + 4 - 1) % 4
        if result == 'OXYGEN':
            break
    print_board(board)
    board[loc] = '.'
    board[(0, 0)] = '.'
    g = build_graph(board)
    return shortest_path_to_oxygen(g, loc)


def test_solve1():
    assert solve1() == 380


def test_solve2():
    assert solve2() == 410


if __name__ == "__main__":
    solve2()
