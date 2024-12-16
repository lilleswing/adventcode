import networkx as nx
from networkx.algorithms.shortest_paths.generic import all_shortest_paths

directions = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1)
}


def parse(fname):
    g = nx.DiGraph()
    lines = open(fname).readlines()
    lines = [x.strip() for x in lines]
    source, sink = None, None
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] == 'S':
                source = (r, c, 'E')
            elif lines[r][c] == 'E':
                sink = (r, c, '*')
            square_char = lines[r][c]
            if lines[r][c] == '#':
                continue
            for dir_name, (dr, dc) in directions.items():
                nr, nc = r + dr, c + dc
                new_char = lines[nr][nc]
                if new_char == '.':
                    g.add_edge((r, c, dir_name), (nr, nc, dir_name), weight=1)
                elif new_char == 'E':
                    g.add_edge((r, c, dir_name), (nr, nc, '*'), weight=1)
            # add edges for spinning around
            g.add_edge((r, c, 'N'), (r, c, 'E'), weight=1_000)
            g.add_edge((r, c, 'E'), (r, c, 'S'), weight=1_000)
            g.add_edge((r, c, 'S'), (r, c, 'W'), weight=1_000)
            g.add_edge((r, c, 'W'), (r, c, 'N'), weight=1_000)

            g.add_edge((r, c, 'N'), (r, c, 'W'), weight=1_000)
            g.add_edge((r, c, 'W'), (r, c, 'S'), weight=1_000)
            g.add_edge((r, c, 'S'), (r, c, 'E'), weight=1_000)
            g.add_edge((r, c, 'E'), (r, c, 'N'), weight=1_000)
    return g, source, sink


def get_weigted_path_len(g, path):
    total_weigtht = 0
    for i in range(len(path) - 1):
        total_weigtht += g[path[i]][path[i + 1]]['weight']
    return total_weigtht


def part1(fname):
    g, source, sink = parse(fname)
    path_lens = []
    path = nx.shortest_path(g, source, sink, weight='weight')
    path_lens.append(get_weigted_path_len(g, path))
    print(min(path_lens))


def part2(fname):
    g, source, sink = parse(fname)
    used = set()
    all_shortest_paths = nx.all_shortest_paths(g, source, sink, weight='weight')
    print("all shortest paths calculated")
    for path in all_shortest_paths:
        for node in path:
            square = (node[0], node[1])
            used.add(square)
    print(len(used))


if __name__ == "__main__":
    part1('day16.in')
    part2('day16.in')
