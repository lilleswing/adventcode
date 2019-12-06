def read_file(fname):
    with open(fname) as fin:
        return [x.strip() for x in fin.readlines()]


OPEN = '.'
TREE = '|'
LUMBER = '#'


def get_neighbors(board, r, c):
    retval = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            cr, cc = r + dr, c + dc
            if dr == 0 and dc == 0:
                continue
            if cr < 0 or cc < 0:
                continue
            if cr >= len(board) or cc >= len(board[0]):
                continue
            retval.append(board[cr][cc])
    return retval


def three_or_more_trees(board, r, c):
    neighbors = get_neighbors(board, r, c)
    num_trees = sum([1 for x in neighbors if x == TREE])
    return num_trees >= 3


def three_or_more_lumber(board, r, c):
    neighbors = get_neighbors(board, r, c)
    num_lumber = sum([1 for x in neighbors if x == LUMBER])
    return num_lumber >= 3


def at_least_one_lumber_and_at_least_one_tree(board, r, c):
    neighbors = get_neighbors(board, r, c)
    num_lumber = sum([1 for x in neighbors if x == LUMBER])
    num_trees = sum([1 for x in neighbors if x == TREE])
    return num_lumber >= 1 and num_trees >= 1


def calc_new_pixel(board, r, c):
    if board[r][c] == OPEN:
        if three_or_more_trees(board, r, c):
            return TREE
        else:
            return OPEN
    if board[r][c] == TREE:
        if three_or_more_lumber(board, r, c):
            return LUMBER
        else:
            return TREE

    if board[r][c] == LUMBER:
        if at_least_one_lumber_and_at_least_one_tree(board, r, c):
            return LUMBER
        else:
            return OPEN


def count_squares(board, pixel):
    total = 0
    for row in board:
        for square in row:
            if square == pixel:
                total += 1
    return total


def solve1():
    board = read_file('day18.in')
    board = [list(x) for x in board]
    for i in range(10):
        new_board = []
        for r, row in enumerate(board):
            new_row = []
            for c, col in enumerate(row):
                new_pixel = calc_new_pixel(board, r, c)
                new_row.append(new_pixel)
            new_board.append(new_row)
        board = new_board
    num_lumber = count_squares(board, LUMBER)
    num_trees = count_squares(board, TREE)
    print(num_lumber, num_trees)
    return num_lumber * num_trees


def calculate_distance_and_offset():
    board = read_file('day18.in')
    board = [list(x) for x in board]
    seen = {}
    last_key = None
    for i in range(700):
        new_board = []
        for r, row in enumerate(board):
            new_row = []
            for c, col in enumerate(row):
                new_pixel = calc_new_pixel(board, r, c)
                new_row.append(new_pixel)
            new_board.append(new_row)
        board = new_board
        num_lumber = count_squares(board, LUMBER)
        num_trees = count_squares(board, TREE)
        key = (num_lumber, num_trees)
        last_key = key
        if key not in seen:
            seen[key] = list()
        seen[key].append(i + 1)
    l = seen[last_key]
    return l[-2], l[-1], board


def solve2():
    offset, next_val, board = calculate_distance_and_offset()
    goal = 1000000000
    goal -= offset
    period = next_val - offset
    goal = goal % period

    print(goal, period)
    for i in range(goal):
        new_board = []
        for r, row in enumerate(board):
            new_row = []
            for c, col in enumerate(row):
                new_pixel = calc_new_pixel(board, r, c)
                new_row.append(new_pixel)
            new_board.append(new_row)
        board = new_board
    num_lumber = count_squares(board, LUMBER)
    num_trees = count_squares(board, TREE)
    print(num_lumber, num_trees)
    return num_lumber * num_trees


def test_solve1():
    assert solve1() == 645946


def test_solve2():
    assert solve2() == 227688
