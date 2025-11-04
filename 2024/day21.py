import networkx as nx
from functools import lru_cache


class Robot(object):
    def __init__(self):
        g = nx.DiGraph()
        # Horizontal edges
        g.add_edge('7', '8', direction='>')
        g.add_edge('8', '9', direction='>')
        g.add_edge('4', '5', direction='>')
        g.add_edge('5', '6', direction='>')
        g.add_edge('1', '2', direction='>')
        g.add_edge('2', '3', direction='>')
        g.add_edge('0', 'A', direction='>')

        g.add_edge('9', '8', direction='<')
        g.add_edge('8', '7', direction='<')
        g.add_edge('6', '5', direction='<')
        g.add_edge('5', '4', direction='<')
        g.add_edge('3', '2', direction='<')
        g.add_edge('2', '1', direction='<')
        g.add_edge('A', '0', direction='<')

        # Vertical edges
        g.add_edge('7', '4', direction='v')
        g.add_edge('8', '5', direction='v')
        g.add_edge('9', '6', direction='v')
        g.add_edge('4', '1', direction='v')
        g.add_edge('5', '2', direction='v')
        g.add_edge('6', '3', direction='v')
        g.add_edge('2', '0', direction='v')
        g.add_edge('3', 'A', direction='v')

        g.add_edge('0', '2', direction='^')
        g.add_edge('A', '3', direction='^')
        g.add_edge('1', '4', direction='^')
        g.add_edge('2', '5', direction='^')
        g.add_edge('3', '6', direction='^')
        g.add_edge('4', '7', direction='^')
        g.add_edge('5', '8', direction='^')
        g.add_edge('6', '9', direction='^')
        self.g = g

    def get_all_paths(self, from_char, to_char):
        if from_char == to_char:
            return [tuple()]
        try:
            all_paths = list(nx.all_shortest_paths(self.g, from_char, to_char))
        except nx.NetworkXNoPath:
            return [tuple()]

        result = []
        for path in all_paths:
            dirs = []
            for i in range(1, len(path)):
                e = self.g[path[i - 1]][path[i]]
                dirs.append(e['direction'])
            result.append(tuple(dirs))
        return result


class Robot2(object):
    def __init__(self):
        g = nx.DiGraph()
        g.add_edge('^', 'A', direction='>')
        g.add_edge('<', 'v', direction='>')
        g.add_edge('v', '>', direction='>')

        g.add_edge('A', '^', direction='<')
        g.add_edge('>', 'v', direction='<')
        g.add_edge('v', '<', direction='<')

        g.add_edge('^', 'v', direction='v')
        g.add_edge('A', '>', direction='v')

        g.add_edge('v', '^', direction='^')
        g.add_edge('>', 'A', direction='^')
        self.g = g

    def get_all_paths(self, from_char, to_char):
        if from_char == to_char:
            return [tuple()]
        try:
            all_paths = list(nx.all_shortest_paths(self.g, from_char, to_char))
        except nx.NetworkXNoPath:
            return [tuple()]

        result = []
        for path in all_paths:
            dirs = []
            for i in range(1, len(path)):
                e = self.g[path[i - 1]][path[i]]
                dirs.append(e['direction'])
            result.append(tuple(dirs))
        return result


# Global instances
numeric_robot = Robot()
directional_robot = Robot2()


@lru_cache(maxsize=None)
def min_cost_for_transition(from_btn, to_btn, depth, is_numeric=False):
    """
    Compute the minimum cost to move from from_btn to to_btn and press it,
    given that there are 'depth' layers of directional keypads above this one.

    If depth == 0, we're at the topmost level (you), so cost is just the sequence length.
    If depth > 0, we need to compute the cost recursively.
    """
    robot = numeric_robot if is_numeric else directional_robot

    # Get all possible shortest paths from from_btn to to_btn
    all_paths = robot.get_all_paths(from_btn, to_btn)

    if depth == 0:
        # At the top level (you), just count the moves plus the A press
        return min(len(path) + 1 for path in all_paths)

    # For each possible path, compute the cost of typing it on the next level up
    min_cost = float('inf')

    for path in all_paths:
        # Need to type this path plus an 'A' on the directional keypad above
        sequence = list(path) + ['A']

        # Start at 'A' on the upper keypad
        cost = 0
        current = 'A'

        for next_btn in sequence:
            cost += min_cost_for_transition(current, next_btn, depth - 1, is_numeric=False)
            current = next_btn

        min_cost = min(min_cost, cost)

    return min_cost


def solve(fname, num_directional_robots):
    """
    Solve for a given number of directional robots.
    For part 1: num_directional_robots = 2
    For part 2: num_directional_robots = 25
    """
    lines = open(fname).readlines()
    lines = [x.strip() for x in lines]
    lines = [[y for y in x] for x in lines if x]
    retval = []

    for line in lines:
        code = int("".join([c for c in line if c.isdigit()]))

        # Compute the cost for typing this code on the numeric keypad
        # with num_directional_robots layers above it
        total_cost = 0
        current = 'A'

        for next_btn in line:
            cost = min_cost_for_transition(current, next_btn, num_directional_robots, is_numeric=True)
            total_cost += cost
            current = next_btn

        print(f"{''.join(line)}: length={total_cost}, code={code}")
        retval.append((total_cost, code))

    total = 0
    for r in retval:
        print(r)
        total += r[0] * r[1]
    print(f"Sum of complexities: {total}")
    return total


def part1(fname):
    return solve(fname, 2)


def part2(fname):
    return solve(fname, 25)


if __name__ == "__main__":
    print("=== Part 1 ===")
    part1('day21.in')
    print("\n=== Part 2 ===")
    part2('day21.in')
