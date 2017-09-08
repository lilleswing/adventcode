import re
import networkx as nx


class Node(object):
  def __init__(self, x, y, size, used, avail):
    self.x = x
    self.y = y
    self.size = size
    self.used = used
    self.avail = avail

  def __repr__(self):
    return "%s,%s,%s,%s,%s" % (self.x, self.y, self.size, self.used, self.avail)


def parse_nodes():
  lines = [x.strip() for x in open('day22.in').readlines()]
  lines = lines[2:]
  nodes = list()
  for line in lines:
    m = re.match(r".*x(\d+)-y(\d+) +(\d+)T +(\d+)T +(\d+)T.*", line)
    node = Node(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))
    nodes.append(node)
  return nodes


def is_vp(a, b):
  if a.used <= 0:
    return False
  if a.x == b.x and a.y == b.y:
    return False
  return a.used < b.avail


def solve1():
  nodes = parse_nodes()
  vp = 0
  for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
      if is_vp(nodes[i], nodes[j]):
        vp += 1
      if is_vp(nodes[j], nodes[i]):
        vp += 1
  return vp


def is_hole(node, lookup):
  if node.used == 0:
    return True
  return False


def gen_key(t):
  return str(t)


def solve2():
  nodes = parse_nodes()
  lookup = {}
  for node in nodes:
    lookup[(node.y, node.x)] = node

  s = ""
  starting_point = None
  for row in range(31):
    for col in range(31):
      node = lookup[(row, col)]
      if is_hole(node, lookup):
        starting_point = node
        s += "_"
      elif node.used > 75:
        s += "#"
      else:
        s += "."
    print(s)
    s = ""
  g = nx.DiGraph()
  for row in range(31):
    for col in range(31):
      for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_d = row + d[0], col + d[1]
        if new_d not in lookup:
          continue
        node, neighbor = lookup[(row, col)], lookup[new_d]
        if node.used < 100 and neighbor.used < 100:
          g.add_edge((row, col), new_d)
  moves = 0
  goal = 29
  starting_point = (starting_point.y, starting_point.x)
  while goal >= 0:
    path = nx.astar_path(g, starting_point, (0, goal))
    moves += len(path) + 1
    starting_point = (0, goal+1)
    goal -= 1
  return moves


if __name__ == "__main__":
  print(solve1())
  print(solve2())
