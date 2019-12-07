from functools import lru_cache
import networkx as nx
from networkx.algorithms.shortest_paths.generic import shortest_path
from networkx.algorithms.shortest_paths.weighted import dijkstra_path

seen = set()


@lru_cache(None)
def gi_index(x, y, depth, target):
    if x < 0 or y < 0:
        raise ValueError()
    if (x, y) in seen:
        raise ValueError()
    seen.add((x, y))
    if x == target[0] and y == target[1]:
        return 0
    if x == 0 and y == 0:
        return 0
    if y == 0:
        return x * 16807
    if x == 0:
        return y * 48271
    return erosion_level(x - 1, y, depth, target) * erosion_level(x, y - 1, depth, target)


@lru_cache(None)
def erosion_level(x, y, depth, target):
    el = gi_index(x, y, depth, target) + depth
    el = el % 20183
    return el


def pixel_type(x, y, depth, target):
    return erosion_level(x, y, depth, target) % 3


ROCKY = "."
WET = "="
NARROW = "|"
LOOKUP = {
    0: ".",
    1: "=",
    2: "|"
}


def make_board(target, depth):
    board = []
    for y in range(target[1] + 100):
        row = []
        for x in range(target[0] + 100):
            ei = pixel_type(x, y, depth, target)
            row.append(LOOKUP[ei])
        board.append(row)
    return board


def get_adj_squares(x, y, board, acceptable):
    bh = len(board)
    bw = len(board[0])
    retval = []
    for dy, dx in [[-1, 0],
                   [1, 0],
                   [0, -1],
                   [0, 1]]:
        cx, cy = x + dx, y + dy
        if cx < 0 or cy < 0:
            continue
        if cx >= bw or cy >= bh:
            continue
        pixel = board[cy][cx]
        if pixel in acceptable:
            retval.append((cx, cy))
    return retval


def add_transitions_to_graph(g, board, allowable, equipment):
    """
    :param allowable: list of str
        List of characters we can move between
    :param equipment: chr
        ['n', 't', 'c']
        what equipment we have equiped

    :return:
    """
    height = len(board)
    width = len(board[0])
    for y in range(height):
        for x in range(width):
            my_pixel = board[y][x]
            if my_pixel not in allowable:
                continue
            neighbors = get_adj_squares(x, y, board, allowable)
            for neighbor in neighbors:
                nx, ny = neighbor
                my_state = (x, y, equipment)
                their_state = (nx, ny, equipment)
                g.add_edge(my_state, their_state, weight=1)


def make_graph(board):
    # n, t, c
    height = len(board)
    width = len(board[0])

    g = nx.Graph()

    # Equiping Transitions
    for y in range(height):
        for x in range(width):
            n = (x, y, 'n')
            t = (x, y, 't')
            c = (x, y, 'c')
            pixel = board[y][x]
            if pixel == ROCKY:
                g.add_edge(t, c, weight=7)
            if pixel == WET:
                g.add_edge(c, n, weight=7)
            if pixel == NARROW:
                g.add_edge(t, n, weight=7)

    add_transitions_to_graph(g, board, [WET, NARROW], 'n')
    add_transitions_to_graph(g, board, [ROCKY, NARROW], 't')
    add_transitions_to_graph(g, board, [ROCKY, WET], 'c')
    return g


def print_board(board, target):
    retval = ""
    for r, row in enumerate(board):
        s = ""
        for c, pixel in enumerate(board[r]):
            if r == target[0] and c == target[1]:
                s += "T"
            else:
                s += pixel
        retval += s + "\n"
    print(retval)


def solve2():
    depth = 10914
    target = (9, 739)

    # depth = 510
    # target = (10, 10)
    # target = (1, 0)

    board = make_board(target, depth)
    if board[target[1]][target[0]] != ROCKY:
        raise ValueError()
    graph = make_graph(board)
    print_board(board, target)

    start_state = (0, 0, 't')
    end_state = (target[0], target[1], 't')

    path = dijkstra_path(graph, start_state, end_state, weight='weight')
    total_weight = 0
    for i in range(1, len(path)):
        from_node, to_node = path[i - 1], path[i]
        nx, ny = to_node[0], to_node[1]
        total_weight += graph.get_edge_data(from_node, to_node)['weight']
        print(to_node, board[ny][nx], total_weight)
        # print(from_node, to_node)
    return total_weight


def solve1():
    depth = 10914
    target = (9, 739)

    # depth = 510
    # target = (10, 10)

    total = 0
    board = []
    for y in range(target[1] + 1):
        row = []
        for x in range(target[0] + 1):
            ei = pixel_type(x, y, depth, target)
            total += ei
            row.append(LOOKUP[ei])
        board.append(row)
    # total -= pixel_type(0, 0, depth, target)
    # total -= pixel_type(target[0], target[1], depth)
    for row in board:
        print("".join(row))
    return total


def test_solve2():
    assert solve2() == 1013


def test_solve1():
    assert solve1() == 7380
