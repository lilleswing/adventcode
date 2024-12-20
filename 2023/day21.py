import networkx as nx
from mypy.binder import defaultdict


def make_graph(fname):
    lines = [x.strip() for x in open(fname).readlines()]
    g = nx.Graph()
    source = None
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == '#':
                continue
            if lines[r][c] == 'S':
                source = (r, c)
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= len(lines) or nc < 0 or nc >= len(lines[0]):
                    continue
                if lines[nr][nc] == '.':
                    g.add_edge((r, c), (nr, nc), weight=1)
    return g, source

def part1(fname):
    if fname.endswith('sample'):
        n_rounds = 6
    else:
        n_rounds = 64
    g, source = make_graph(fname)
    print(g, source)
    d = defaultdict(lambda: set())
    d[0] = set([source])
    for i in range(1, n_rounds + 1):
        for node in d[i - 1]:
            for neighbor in g.neighbors(node):
                d[i].add(neighbor)
    print(len(d[n_rounds]))

if __name__ == "__main__":
    part1('day21.in')
    # part1('day24.in')
