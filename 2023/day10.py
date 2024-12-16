import networkx as nx
from collections import defaultdict

import tqdm


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
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
        'S': [(1, 0), (-1, 0), (0, 1), (0, -1)]
    }
    d = defaultdict(lambda: '.')
    lines = [x.strip() for x in open(fname).readlines()]
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            d[(r, c)] = lines[r][c]
    source = None
    edges = set()
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            my_c = d[(r, c)]
            if my_c == 'S':
                source = (r, c)
            if my_c not in edge_patterns:
                continue
            for dr, dc in edge_patterns[my_c]:
                nr, nc = dr + r, dc + c
                edges.add(((r, c), (nr, nc)))
    g = nx.Graph()
    for e in edges:
        v1, v2 = e
        if (v2, v1) in edges:
            g.add_edge(v1, v2)
    return g, source


def print_it(g, source):
    _, dist = nx.bellman_ford_predecessor_and_distance(g, source)
    max_r, max_c = max(g.nodes, key=lambda x: x[0])[0], max(g.nodes, key=lambda x: x[1])[1]
    for r in range(max_r + 1):
        for c in range(max_c + 1):
            if (r, c) in dist:
                print(dist[(r,c)], end='')
            else:
                print('.', end='')
        print()


def part1(fname):
    g, source = parse_graph(fname)
    loops = [x for x in nx.simple_cycles(g)]
    loop = [x for x in loops if source in x][0]
    _, dist = nx.bellman_ford_predecessor_and_distance(g, source)
    dists = [dist[x] for x in loop]
    print(max(dists))

def part2(fname):
    from shapely.geometry import Point
    from shapely.geometry.polygon import Polygon
    g, source = parse_graph(fname)
    loops = [x for x in nx.simple_cycles(g)]
    loop = [x for x in loops if source in x][0]
    polygon =  Polygon(loop)

    lines = [x.strip() for x in open(fname).readlines()]
    total = 0

    display = ""
    for r in tqdm.tqdm(range(len(lines))):
        for c in range(len(lines[0])):
            if polygon.contains(Point(r, c)):
                total += 1
                display += 'I'
            elif (r, c) in loop:
                display += 'X'
            else:
                display += '.'
        display += "\n"
    print(display)
    print(total)

if __name__ == "__main__":
    # part1('day10.in')
    part2('day10.in')
