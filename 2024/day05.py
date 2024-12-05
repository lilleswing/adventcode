import networkx as nx

def parse(fname):
    lines = open(fname).readlines()
    lines = [x.strip() for x in lines]
    rules = []
    while lines[0].find('|') != -1:
        v0, v1 = lines[0].split('|')
        v0, v1 = int(v0), int(v1)
        rules.append((v0,v1))
        lines = lines[1:]
    lines = lines[1:]
    manuals = []
    for line in lines:
        l = line.split(',')
        l = [int(x) for x in l]
        manuals.append(l)
    return rules, manuals


def check1(rules, manual):
    idx_lookup = {x:y for x, y in zip(manual, range(len(manual)))}
    for rule in rules:
        v1, v2 = rule
        if v1 not in idx_lookup or v2 not in idx_lookup:
            continue
        idx1, idx2 = idx_lookup[v1], idx_lookup[v2]
        if idx2 < idx1:
            return False
    return True

def part1(rules, manuals):
    total = 0
    for manual in manuals:
        if check1(rules, manual):
            idx = len(manual) // 2
            total += manual[idx]
    print(total)
    return total


def topo_sort_it(rules, manual):
    g = nx.DiGraph()
    idx_lookup = {x:y for x, y in zip(manual, range(len(manual)))}

    for rule in rules:
        v1, v2 = rule
        if v1 not in idx_lookup or v2 not in idx_lookup:
            continue
        g.add_edge(v1,v2)
    order = [x for x in nx.topological_sort(g)]
    assert len(order) == len(manual)
    return order



def part2(rules, manuals):
    total = 0
    for manual in manuals:
        if check1(rules, manual):
            continue
        l = topo_sort_it(rules, manual)
        idx = len(manual) // 2
        total += l[idx]
    print(total)
    return total

if __name__ == "__main__":
    rules, manuals = parse('day05.in')
    part1(rules, manuals)
    part2(rules, manuals)
