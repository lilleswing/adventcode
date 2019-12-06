import networkx as nx
from networkx.algorithms.shortest_paths.generic import shortest_path

from . import read_file


def solve1():
    lines = read_file('day6.in')
    g = nx.DiGraph()
    for line in lines:
        v1, v2 = line.split(')')
        g.add_edge(v2, v1)

    total = 0
    for elem in g.nodes:
        neighbors = list(g.neighbors(elem))
        while len(neighbors) != 0:
            total += 1
            neighbors = list(g.neighbors(neighbors[0]))
    return total


def solve2():
    lines = read_file('day6.in')

    g = nx.Graph()
    for line in lines:
        v1, v2 = line.split(')')
        g.add_edge(v2, v1)
    my_path = shortest_path(g, 'SAN', 'YOU')
    return len(my_path) - 3


def test_solve1():
    assert solve1() == 160040


def test_solve2():
    assert solve2() == 373
