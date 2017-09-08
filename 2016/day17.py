import hashlib

problem_input = "awrkjxxr"

MOVES = {
  "D": (0, 1),
  "U": (0, -1),
  "R": (1, 0),
  "L": (-1, 0)
}
OPEN = {'b', 'c', 'd', 'e', 'f'}


def md5(path):
  m = hashlib.md5()
  m.update(bytes(path, encoding='UTF-8'))
  s = m.hexdigest()
  return s


def get_move(loc, c):
  move = MOVES[c]
  new_loc = (loc[0] + move[0], loc[1] + move[1])
  if new_loc[0] < 0 or new_loc[0] >= 4 or new_loc[1] < 0 or new_loc[1] >= 4:
    return None
  return c, new_loc


def get_moves(loc, path):
  moves = []
  h = md5(path)
  if h[1] in OPEN:
    moves.append(get_move(loc, 'D'))
  if h[3] in OPEN:
    moves.append(get_move(loc, 'R'))
  if h[2] in OPEN:
    moves.append(get_move(loc, 'L'))
  if h[0] in OPEN:
    moves.append(get_move(loc, 'U'))
  return [y for y in filter(lambda x: x is not None, moves)]


def dfs(loc, path):
  if loc == (3, 3):
    return True, path
  moves = get_moves(loc, path)
  is_solved, solved_path, max_len = False, "FAILURE", float('inf')
  for my_dir, new_loc in moves:
    retval, new_path = dfs(new_loc, "%s%s" % (path, my_dir))
    if retval and len(new_path) < max_len:
      is_solved, max_len, solved_path = True, len(new_path), new_path
  return is_solved, solved_path


def dfs_longest(loc, path):
  if loc == (3, 3):
    return True, path
  moves = get_moves(loc, path)
  is_solved, solved_path, min_len = False, "FAILURE", 0
  for my_dir, new_loc in moves:
    retval, new_path = dfs_longest(new_loc, "%s%s" % (path, my_dir))
    if retval and len(new_path) > min_len:
      is_solved, min_len, solved_path = True, len(new_path), new_path
  return is_solved, solved_path


def solve1():
  loc = (0, 0)
  solved, path = dfs(loc, problem_input)
  return path


def solve2():
  loc = (0, 0)
  solved, path = dfs_longest(loc, problem_input)
  return len(path[len(problem_input):])


if __name__ == "__main__":
  print(solve1())
  print(solve2())
