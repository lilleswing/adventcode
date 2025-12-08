import numpy as np
import networkx as nx

IN_FILE = 'day08.sample'
N_EDGES = 10

IN_FILE = 'day08.in'
N_EDGES = 1_000

class Point(object):
    def __init__(self, x, y, z):
        self.id = f"{x},{y},{z}"
        self.loc = np.array([x, y, z])

    def distance(self, other):
        return np.linalg.norm(self.loc - other.loc)

    @property
    def x(self):
        return self.loc[0]

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


def part1():
    lines = open(IN_FILE).readlines()
    lines = [x.strip() for x in lines]
    points = []
    for l in lines:
        x, y, z = l.split(',')
        x, y, z = int(x), int(y), int(z)
        points.append(Point(x, y, z))
    g = nx.Graph()
    for idx, _ in enumerate(points):
        g.add_node(idx)

    edges = {}
    for i in range(len(points)):
        p1 = points[i]
        for j in range(i+1, len(points)):
            p2 = points[j]
            edges[(i, j)] = p1.distance(p2)
    edges = sorted(edges.items(), key=lambda x: x[1])
    for e, d in edges[:N_EDGES]:
        p1, p2 = e
        g.add_edge(p1, p2, weight=d)
    components = list(nx.connected_components(g))
    components = sorted(components, key=lambda x: len(x), reverse=True)
    total = len(components[0]) * len(components[1]) * len(components[2])
    print(total)

def part2():
    lines = open(IN_FILE).readlines()
    lines = [x.strip() for x in lines]
    points = []
    for l in lines:
        x, y, z = l.split(',')
        x, y, z = int(x), int(y), int(z)
        points.append(Point(x, y, z))
    g = nx.Graph()
    for idx, _ in enumerate(points):
        g.add_node(idx)

    edges = {}
    for i in range(len(points)):
        p1 = points[i]
        for j in range(i+1, len(points)):
            p2 = points[j]
            edges[(i, j)] = p1.distance(p2)
    edges = sorted(edges.items(), key=lambda x: x[1])
    for e, d in edges:
        p1, p2 = e
        g.add_edge(p1, p2, weight=d)
        components = list(nx.connected_components(g))
        if len(components) == 1:
            break
    print(e, d)
    p1, p2 = points[e[0]], points[e[1]]
    print(p1.x * p2.x)


if __name__ == "__main__":
    # part1()
     part2()
