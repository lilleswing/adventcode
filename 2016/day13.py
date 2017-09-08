import networkx as nx

rows, cols = 60, 60

# inp = 10
# start = (1, 1)
# goal = (4, 7)

inp = 1362
start = (1, 1)
goal = (39, 31)


def create_board(inp):
  board = list()
  for y in range(rows):
    row = list()
    for x in range(cols):
      val = x * x + 3 * x + 2 * x * y + y + y * y + inp
      val = "{0:b}".format(val).count('1')
      if val % 2 == 0:
        row.append('.')
      else:
        row.append('#')
    board.append(row)
  return board


def display_board(board):
  s = ""
  for row in board:
    s += "".join(row) + "\n"
  print(s)


def check_and_add_edge(g, p1, p2, board):
  if board[p1[0]][p1[1]] == '.' and board[p2[0]][p2[1]] == '.':
    g.add_edge(p1, p2)


def build_graph(board):
  g = nx.Graph()
  for i in range(1, len(board)):
    for j in range(len(board)):
      p1, p2 = (i - 1, j), (i, j)
      check_and_add_edge(g, p1, p2, board)
      p1, p2 = (j, i - 1), (j, i)
      check_and_add_edge(g, p1, p2, board)
  return g


def solve1():
  board = create_board(inp)
  g = build_graph(board)
  path = nx.shortest_path(g, start, goal)
  return len(path) - 1


def solve2():
  board = create_board(inp)
  g = build_graph(board)
  paths = nx.shortest_path(g, start)
  total = 0
  for path in paths.values():
    if len(path) - 1 <= 50:
      total += 1
  return total


if __name__ == "__main__":
  print(solve1())
  print(solve2())
