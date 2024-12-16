import numpy as np


def parse(fname):
    lines = [x.strip() for x in open(fname).readlines()]
    lines = [list(x) for x in lines]
    retval = []
    sample = []
    while len(lines) > 0:
        if len(lines[0]) == 0:
            retval.append(np.array(sample))
            sample = []
            lines.pop(0)
            continue
        sample.append(lines.pop(0))
    retval.append(np.array(sample))
    return retval


def find_reflection(board):
    """
    :param board:
    :return:
    find the reflection of the board
    """
    for r in range(1, board.shape[0]):
        top = board[:r]
        bottom = np.flip(board[r:], axis=0)
        size = min(top.shape[0], bottom.shape[0])
        top = top[-size:, :]
        bottom = bottom[-size:, :]
        # print(r)
        # print(top)
        # print(bottom)
        # print(top==bottom)
        # print()
        if np.all(top == bottom):
            return 100 * r
    for c in range(1, board.shape[1]):
        left = board[:, :c]
        right = np.flip(board[:, c:], axis=1)
        size = min(left.shape[1], right.shape[1])
        left = left[:, -size:]
        right = right[:, -size:]
        if np.all(left == right):
            return c
    return 0


def find_reflection2(board):
    """
    :param board:
    :return:
    find the reflection of the board
    """
    for r in range(1, board.shape[0]):
        top = board[:r]
        bottom = np.flip(board[r:], axis=0)
        size = min(top.shape[0], bottom.shape[0])
        top = top[-size:, :]
        bottom = bottom[-size:, :]
        # print(r)
        # print(top)
        # print(bottom)
        # print(top==bottom)
        # print()
        if np.sum(top != bottom) == 1:
            return 100 * r
    for c in range(1, board.shape[1]):
        left = board[:, :c]
        right = np.flip(board[:, c:], axis=1)
        size = min(left.shape[1], right.shape[1])
        left = left[:, -size:]
        right = right[:, -size:]
        if np.sum(left != right) == 1:
            return c
    return 0


def part1(fname):
    boards = parse(fname)
    total = 0
    for i, b in enumerate(boards):
        v = find_reflection(b)
        if v == 0:
            print(i)
            print(b)
            sys.exit(1)
        total += v
    print(total)


def part2(fname):
    boards = parse(fname)
    total = 0
    for i, b in enumerate(boards):
        v = find_reflection2(b)
        if v == 0:
            print(i)
            print(b)
            sys.exit(1)
        total += v
    print(total)
    pass


if __name__ == "__main__":
    # part1('day13.in')
    part2('day13.in')
