import itertools
import re


class Graph(object):
    def __init__(self):
        self.edges = list()
        self.nodes = set()

    def add_edge(self, from_node, to_node, distance):
        edge1 = Edge(from_node, to_node, distance)
        edge2 = Edge(to_node, from_node, distance)
        self.edges.append(edge1)
        self.edges.append(edge2)
        self.nodes.add(from_node)
        self.nodes.add(to_node)

    def best_walk(self, comparator=lambda x, y: x <= y, initial_value=float('inf')):
        if len(self.nodes) >= 10:
            raise Exception("To large to calculate all permutations")
        best_distance = initial_value
        for permuation in itertools.permutations(self.nodes):
            distance = self._get_walk_distance(permuation)
            if distance is None:
                continue
            if comparator(distance, best_distance):
                best_distance = distance
        return best_distance

    def _get_walk_distance(self, permuation):
        total = 0
        for i in xrange(1, len(permuation)):
            edge = self._get_edge(permuation[i - 1], permuation[i])
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


def parse_edges(lines):
    graph = Graph()
    for line in lines:
        match = re.match("(.+) to (.+) = (\d+)", line)
        graph.add_edge(match.group(1), match.group(2), int(match.group(3)))
    return graph


def solve1(graph):
    return graph.best_walk()


def solve2(graph):
    return graph.best_walk(comparator=lambda x, y: x >= y, initial_value=-1 * float('inf'))


if __name__ == "__main__":
    all_graph = parse_edges([x.strip() for x in open('day9.in').readlines()])
    print(solve1(all_graph))
    print(solve2(all_graph))
