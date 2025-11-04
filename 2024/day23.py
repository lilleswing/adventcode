import networkx as nx
def part1():
    lines = [x.strip() for x in open('day23.in').readlines()]
    g = nx.Graph()
    for l in lines:
        v1, v2 = l.split('-')
        g.add_edge(v1, v2)

    nodes = list(g.nodes)
    total = 0
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            for k in range(j+1, len(nodes)):
                v1, v2, v3 = nodes[i], nodes[j], nodes[k]
                has_t = any([str(x).startswith('t') for x in [v1,v2,v3]])
                if not has_t:
                    continue
                e1 = g.has_edge(v1, v2)
                e2 = g.has_edge(v2, v3)
                e3 = g.has_edge(v1, v3)
                if e1 and e2 and e3:
                    total += 1
    print(total)


def part2():
    lines = [x.strip() for x in open('day23.in').readlines()]
    g = nx.Graph()
    for l in lines:
        v1, v2 = l.split('-')
        g.add_edge(v1, v2)

    print("Finding Cliques")
    components = [x for x in nx.find_cliques(g)]
    print("Call Complete")
    components = sorted(components, key=lambda x: len(x), reverse=True)
    print("In List")
    l = ",".join(sorted(components[0]))
    print(l)


if __name__ == "__main__":
    print("Starting")
    part1()
    part2()