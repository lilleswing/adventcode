from collections import defaultdict
import networkx as nx


def make_board(lines):
    d = defaultdict(lambda: '.')
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            d[(r, c)] = lines[r][c]
    return d


def make_graph(board, lines):
    g = nx.Graph()
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            my_c = board[(r, c)]
            n_perim = 0
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = dr + r, dc + c
                n_c = board[(nr, nc)]
                if n_c == my_c:
                    g.add_edge((r, c), (nr, nc))
                else:
                    n_perim += 1
            g.add_node((r, c))
            nx.set_node_attributes(g, {(r, c): {'perim': n_perim,
                                                'label': my_c}})
    return g


def make_graph2(board, lines):
    dirs = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1)
    }
    g = nx.Graph()
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            my_c = board[(r, c)]
            n_perim = 0
            d = {'label': my_c}
            for l, (dr, dc) in dirs.items():
                nr, nc = dr + r, dc + c
                n_c = board[(nr, nc)]
                if n_c == my_c:
                    g.add_edge((r, c), (nr, nc))
                    d[l] = 0
                else:
                    n_perim += 1
                    d[l] = 1
            g.add_node((r, c))
            nx.set_node_attributes(g, {(r, c): d})
    return g


def score_component(c, g):
    perim_total = sum([g.nodes[x]['perim'] for x in c])
    labels = [g.nodes[x]['label'] for x in c]
    label = labels[0]

    print(label, len(c), perim_total)
    return perim_total * len(c)


def score_component2(c, g):
    dirs = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1)
    }
    c = [x for x in c]
    # construct a new graph with edges between nodes in the component if they share a dir
    total = 0
    for l, (dr, dc) in dirs.items():
        g2 = nx.Graph()
        for x in c:
            if g.nodes[x][l] == 0:
                continue
            neighbors = g.neighbors(x)
            for n in neighbors:
                if g.nodes[n][l] == 1:
                    g2.add_edge(x, n)
            g2.add_node(x)
        sides = nx.connected_components(g2)
        sides = [x for x in sides]
        total += len([x for x in sides])

    labels = [g.nodes[x]['label'] for x in c]
    label = labels[0]
    print(label, len(c), total)
    return len(c) * total


def part1(fname):
    lines = open(fname).readlines()
    lines = [list(x.strip()) for x in lines]
    board = make_board(lines)
    g = make_graph(board, lines)

    total = 0
    for c in nx.connected_components(g):
        total += score_component(c, g)
    print(total)


def part2(fname):
    lines = open(fname).readlines()
    lines = [list(x.strip()) for x in lines]
    board = make_board(lines)
    g = make_graph2(board, lines)

    total = 0
    for c in nx.connected_components(g):
        total += score_component2(c, g)
    print(total)


if __name__ == "__main__":
    #part1("day12.in")
    part2("day12.in")
