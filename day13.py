import itertools
import re


class Graph(object):
    def __init__(self):
        self.edges = list()
        self.nodes = set()
        self.best_permuation = None

    def add_edge(self, from_node, to_node, distance):
        edge1 = Edge(from_node, to_node, distance)
        self.edges.append(edge1)
        self.nodes.add(from_node)
        self.nodes.add(to_node)

    def add_self(self):
        existing_nodes = set(self.nodes)
        for node in existing_nodes:
            self.add_edge("me", node, 0)
            self.add_edge(node, "me", 0)

    def best_hamiltonian(self, comparator=lambda x, y: x <= y, initial_value=float('inf')):
        if len(self.nodes) >= 10:
            raise Exception("To large to calculate all permutations")
        best_distance = initial_value
        for permuation in itertools.permutations(self.nodes):
            distance = self._get_hamiltonian_distance(permuation)
            if distance is None:
                continue
            if comparator(distance, best_distance):
                best_distance = distance
                self.best_permuation = permuation
        return best_distance

    def _get_hamiltonian_distance(self, permuation):
        total = 0
        for i in xrange(0, len(permuation)):
            edge = self._get_edge(permuation[i - 1], permuation[i])
            if edge is None:
                return None
            total += edge.distance
            edge = self._get_edge(permuation[i], permuation[i - 1])
            if edge is None:
                return None
            total += edge.distance
        return total

    def _get_edge(self, from_node, to_node):
        for edge in self.edges:
            if edge.from_node == from_node and edge.to_node == to_node:
                return edge
        return None


class Edge(object):
    def __init__(self, from_node, to_node, distance):
        self.from_node = from_node
        self.to_node = to_node
        self.distance = distance


def make_graph(lines):
    pattern = "(.+) would (.+) (.+) happiness units by sitting next to (.+)\."

    def get_value(m):
        sign = m.group(2) == "gain"
        my_value = int(m.group(3))
        if sign:
            return my_value
        return -1 * my_value

    graph = Graph()
    for line in lines:
        match = re.match(pattern, line)
        value = get_value(match)
        graph.add_edge(match.group(1), match.group(4), value)

    return graph


def solve1(graph):
    return graph.best_hamiltonian(comparator=lambda x, y: x >= y, initial_value=-1000000)


def solve2(graph):
    graph.add_self()
    return graph.best_hamiltonian(comparator=lambda x, y: x >= y, initial_value=-1000000)


if __name__ == "__main__":
    g = make_graph([x.strip() for x in open('day13.in').readlines()])
    print(solve1(g))
    print(solve2(g))
