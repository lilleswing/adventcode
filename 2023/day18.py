import networkx as nx
from collections import defaultdict

from fontTools.ttLib.tables.ttProgram import instructions
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'R': (0, 1),
    'L': (0, -1)
}


def parse(fname):
    lines = [x.strip() for x in open(fname).readlines()]
    lines = [x.strip() for x in lines]
    retval = []
    for line in lines:
        line = line.split(' ')
        line[1] = int(line[1])
        retval.append(line)
    return retval


def print_board(board):
    min_r = min([x[0] for x in board])
    min_c = min([x[1] for x in board])
    max_r = max([x[0] for x in board])
    max_c = max([x[1] for x in board])
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            print(board[(r, c)], end='')
        print()


def flood_fill(board):
    points = []
    for k, v in board.items():
        if v == '#':
            p = Point(k[0], k[1])
            points.append(p)
    poly = Polygon(points)
    min_r = min([x[0] for x in board])
    min_c = min([x[1] for x in board])
    max_r = max([x[0] for x in board])
    max_c = max([x[1] for x in board])
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            if board[(r, c)] == '#':
                continue
            if poly.contains(Point(r, c)):
                board[(r, c)] = '#'
    return board


def get_area(board):
    points = []
    for k, v in board.items():
        if v == '#':
            p = Point(k[0], k[1])
            points.append(p)
    poly = Polygon(points)
    return poly.area


def part1(fname):
    instructions = parse(fname)
    board = defaultdict(lambda: '.')
    robot = (0, 0)
    board[robot] = '#'
    for move in instructions:
        my_dir = directions[move[0]]
        for _ in range(move[1]):
            robot = (robot[0] + my_dir[0], robot[1] + my_dir[1])
            board[robot] = '#'
    print_board(board)
    area = get_area(board)
    # picks theorem -- we really want i + b
    # we know b is the number of '#'
    # solve for i
    # A = i + b/2 - 1
    # i = A - b/2 + 1
    b = 0
    for k, v in board.items():
        if v == '#':
            b += 1
    i = area - b / 2 + 1
    print(i, b, i + b)


def parse2(fname):
    direction_lookup = {
        0: 'R',
        1: 'D',
        2: 'L',
        3: 'U'
    }
    lines = [x.strip() for x in open(fname).readlines()]
    lines = [x.strip() for x in lines]
    retval = []
    for line in lines:
        line = line.split(' ')
        code = line[2]
        code = code[1:-1]
        my_dir = direction_lookup[int(code[-1])]
        my_steps = int(code[1:-1], 16)
        retval.append([my_dir, my_steps])
    return retval


def part2(fname):
    instructions = parse2(fname)
    print(instructions)
    board = defaultdict(lambda: '.')
    robot = (0, 0)
    b = 0
    board[robot] = '#'
    for move in instructions:
        my_dir = directions[move[0]]
        move_len = move[1]
        robot = (robot[0] + my_dir[0] * move_len, robot[1] + my_dir[1] * move_len)
        board[robot] = '#'
        b += move_len
    area = get_area(board)
    i = area - b / 2 + 1
    print(i, b, i + b)


if __name__ == "__main__":
    # part1('day18.in')
    part2('day18.in')
