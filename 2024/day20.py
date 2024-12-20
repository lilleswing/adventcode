from functools import lru_cache

import networkx as nx
from mypy.binder import defaultdict


def make_graph(fname: str) -> tuple[nx.Graph, tuple, tuple]:
    g = nx.Graph()
    lines = open(fname).readlines()
    lines = [x.strip() for x in lines]
    source, sink = None, None
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            ch = lines[r][c]
            if ch == '#':
                continue
            if ch == 'S':
                source = (r, c, 0)
            if ch == 'E':
                sink = (r, c, 0)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= len(lines) or nc < 0 or nc >= len(lines[0]):
                    continue
                c2 = lines[nr][nc]
                if c2 == '#':
                    continue
                g.add_edge((r, c, 0), (nr, nc, 0), weight=1)
    return g, source, sink


@lru_cache(maxsize=None)
def get_jump_deltas(n_steps):
    if n_steps == 0:
        return [(0, 0)]
    existing = get_jump_deltas(n_steps - 1)
    deltas = []
    for p in existing:
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            deltas.append((p[0] + dr, p[1] + dc))
    return deltas


def part1(fname: str) -> None:
    g, source, sink = make_graph(fname)
    print(g, source, sink)
    path = nx.shortest_path(g, source, sink)
    path = path[::-1]
    distance_lookup = {}
    for i, p in enumerate(path):
        distance_lookup[p[:2]] = i

    print(get_jump_deltas(2))
    speedups = defaultdict(int)
    total = 0
    for p in distance_lookup:
        for delta in get_jump_deltas(2):
            new_p = p[0] + delta[0], p[1] + delta[1]
            if new_p not in distance_lookup:
                continue
            speedup = distance_lookup[p] - distance_lookup[new_p] - 2
            if speedup >= 100:
                total += 1
            if speedup > 0:
                speedups[speedup] += 1
    # for k, v in sorted(speedups.items(), key=lambda x: x[0]):
    #     print(v, k)
    print(total)


@lru_cache(maxsize=None)
def get_jump_deltas2(n_steps: int) -> list[tuple[int, int, int]]:
    """
    :param n_steps:
    :return: list of (dr, dc, time_delta)
    """
    if n_steps == 0:
        return [(0, 0, 0)]
    existing = get_jump_deltas2(n_steps - 1)
    used = set()
    for p in existing:
        used.add(p[:2])
    existing = sorted(existing, key=lambda x: x[2])
    deltas = []
    for p in existing:
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = p[0] + dr, p[1] + dc
            if (nr, nc) not in used:
                new_delta = (nr, nc, p[2] + 1)
                deltas.append(new_delta)
                used.add((nr, nc))
    return deltas + get_jump_deltas2(n_steps - 1)


def part2(fname):
    g, source, sink = make_graph(fname)
    path = nx.shortest_path(g, source, sink)
    path = path[::-1]
    distance_lookup = {}
    for i, p in enumerate(path):
        distance_lookup[p[:2]] = i

    speedups = defaultdict(int)
    total = 0
    for p in distance_lookup:
        for delta in get_jump_deltas2(20):
            new_p = p[0] + delta[0], p[1] + delta[1]
            if new_p not in distance_lookup:
                continue
            speedup = distance_lookup[p] - distance_lookup[new_p] - delta[2]
            if speedup >= 100:
                total += 1
            if speedup > 0:
                speedups[speedup] += 1
    # for k, v in sorted(speedups.items(), key=lambda x: x[0]):
    #     print(v, k)
    print(total)


if __name__ == "__main__":
    # part1('day20.in')
    part2('day20.in')
