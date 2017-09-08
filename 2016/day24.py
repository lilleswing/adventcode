from itertools import permutations

import networkx as nx


def manhattan(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])


def lookup(t, board):
  return board[t[0]][t[1]]


def solve1():
  lines = [list(x.strip()) for x in open('day24.in').readlines()]
  beepers = []
  start_point = None
  g = nx.Graph()
  for row in range(len(lines)):
    line = lines[row]
    for col in range(len(line)):
      if lines[row][col] != '#' and lines[row][col] != '.' and lines[row][col] != '0':
        beepers.append((row, col))
      if lines[row][col] == '0':
        start_point = (row, col)
      if lines[row][col] == '#':
        continue
      for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nrow, ncol = row + d[0], col + d[1]
        if lines[nrow][ncol] == '#':
          continue
        g.add_edge((row, col), (nrow, ncol))
  beepers = sorted(beepers, key=lambda x: manhattan(x, start_point))
  print(beepers)
  best_dist = float('inf')
  for path in permutations(beepers):
    my_start = start_point
    my_dist = 0
    for elem in path:
      segment = nx.astar_path(g, my_start, elem, heuristic=manhattan)
      my_start = elem
      my_dist += len(segment) - 1
    if my_dist < best_dist:
      best_dist = my_dist
    print(best_dist)
  return best_dist


def solve2():
  lines = [list(x.strip()) for x in open('day24.in').readlines()]
  beepers = []
  start_point = None
  g = nx.Graph()
  for row in range(len(lines)):
    line = lines[row]
    for col in range(len(line)):
      if lines[row][col] != '#' and lines[row][col] != '.' and lines[row][col] != '0':
        beepers.append((row, col))
      if lines[row][col] == '0':
        start_point = (row, col)
      if lines[row][col] == '#':
        continue
      for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nrow, ncol = row + d[0], col + d[1]
        if lines[nrow][ncol] == '#':
          continue
        g.add_edge((row, col), (nrow, ncol))
  beepers = sorted(beepers, key=lambda x: manhattan(x, start_point))
  print(beepers)
  best_dist = float('inf')
  for path in permutations(beepers):
    my_start = start_point
    my_dist = 0
    for elem in path:
      segment = nx.astar_path(g, my_start, elem, heuristic=manhattan)
      my_start = elem
      my_dist += len(segment) - 1
    segment = nx.astar_path(g, my_start, start_point, heuristic=manhattan)
    my_dist += len(segment) - 1
    if my_dist < best_dist:
      best_dist = my_dist
    print(best_dist)
  return best_dist


if __name__ == "__main__":
  print(solve1())
  print(solve2())
