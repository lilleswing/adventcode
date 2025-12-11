import networkx as nx
from collections import deque

def parse(lines):
    g = nx.DiGraph()
    for line in lines:
        line = line.strip()
        n, r = line.split(':')
        r = r.strip().split(' ')
        for e in r:
            g.add_edge(n, e)
    return g

def part1():
    lines = open('day11.in').readlines()
    g = parse(lines)
    paths = [x for x in nx.all_simple_paths(g, 'you', 'out')]
    print(paths)
    print(len(paths))

memoize = {}
def count_paths_dp(g, source, sink, exclude):
    if (source, sink, exclude) in memoize:
        return memoize[(source, sink, exclude)]
    if source == sink:
        return 1

    total = 0
    for n2 in g[source]:
        if n2 in exclude:
            continue
        total += count_paths_dp(g, n2, sink, exclude)
    memoize[(source, sink, exclude)] = total
    return total

def part2():
    """
    svr->dac->fft->out
    svr->fft->dac->out
    :return:
    """
    lines = open('day11.in').readlines()
    g = parse(lines)
    p1 = count_paths_dp(g, 'svr', 'dac', ('out', 'fft')) * \
         count_paths_dp(g, 'dac', 'fft', ('svr', 'out')) * \
         count_paths_dp(g, 'fft', 'out', ('svr', 'dac'))
    print(p1)

    p2 = count_paths_dp(g, 'svr', 'fft', ('dact', 'out')) * \
         count_paths_dp(g, 'fft', 'dac', ('svr', 'out')) * \
         count_paths_dp(g, 'dac', 'out', ('svr', 'fft'))
    print(p2)
    print(p1 + p2)





if __name__ == "__main__":
    #part1()
    part2()
