import networkx as nx
from collections import defaultdict
def parse_graph(fname):
    """

    :param fname:
    :return:
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    """
    # layout row, col
    edge_patterns = {
        "|": [(1, 0), (-1, 0)],
        "-": [(0, 1), (0, -1)],
        "L": [(1, 0), (0, 1)],
        "J": [(1, 0), (0, -1)],
        "7": [(-1, 0), (0, -1)],
        "F": [(-1, 0), (0, 1)],
        'S': []
    }
    d = defaultdict(lambda: '.')
    lines = open(fname).readlines()
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            d[(r, c)] = lines[r][c]
    g = nx.Graph()
    source = None
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            my_c = d[(r, c)]
            if my_c == 'S':
                source = (r, c)
            if my_c not in edge_patterns:
                continue
            for dr, dc in edge_patterns[my_c]:
                nr, nc = dr + r, dc + c
                n_c = d[(nr, nc)]
                if n_c in edge_patterns:
                    g.add_edge((r, c), (nr, nc))
    return g, source

def part1(fname):
    g, source = parse_graph(fname)


if __name__ == "__main__":
    part1('day10.sample')