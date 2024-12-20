from collections import defaultdict
import networkx as nx


def make_graph(fname, row_len, col_len, num_squares=1024):
    d = defaultdict(lambda: '#')
    for r in range(row_len):
        for c in range(col_len):
            d[(r, c)] = '.'
    lines = open(fname).readlines()
    lines = [x.strip() for x in lines]
    lines = [[int(y) for y in x.split(',')] for x in lines]
    for r, c in lines[:num_squares]:
        d[(r, c)] = '#'
    # print_board(d, row_len, col_len)

    g = nx.Graph()
    for r in range(row_len):
        for c in range(col_len):
            if d[(r, c)] == '#':
                continue
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if d[(nr, nc)] == '.':
                    g.add_edge((r, c), (nr, nc), weight=1)
    return g, (0, 0), (row_len - 1, col_len - 1)


def print_board(d, row_len, col_len):
    """
    :param d:
    :param row_len:
    :param col_len:
    :return:

    """
    for r in range(row_len):
        for c in range(col_len):
            print(d[(r, c)], end='')
        print()

def part1(fname):
    if fname == 'day18.sample':
        row_len = 7
        col_len = 7
        num_squares = 12
    else:
        row_len = 71
        col_len = 71
        num_squares = 1024
    g, source, sink = make_graph(fname, row_len, col_len, num_squares)
    steps = nx.shortest_path_length(g, source, sink)
    print(steps)

def part2(fname):
    row_len = 71
    col_len = 71
    for i in range(1024, 1_000_000_000):
        g, source, sink = make_graph(fname, row_len, col_len, i)
        try:
            steps = nx.shortest_path_length(g, source, sink)
        except:
            break
    lines = [x.strip() for x in open(fname).readlines()]
    print(lines[i-1])


if __name__ == "__main__":
    #part1('day18.in')
    part2('day18.in')
