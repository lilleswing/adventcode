import hashlib

problem_input = "ihgpwlah"

MOVES = {
  "D": (0, 1),
  "U": (0, -1),
  "R": (1, 0),
  "L": (-1, 0)
}
OPEN = {'a', 'b', 'c', 'd', 'e', 'f'}


def md5(path):
  m = hashlib.md5()
  m.update(bytes("%s%s" % (input, path), encoding='UTF-8'))
  s = m.hexdigest()
  return s


def get_move(loc, c):
  move = MOVES[c]
  new_loc = (loc[0] + move[0], loc[1] + move[1])
  if new_loc == (4, 3):
    return c, new_loc
  if new_loc[0] < 0 or new_loc[0] >= 4 or new_loc[1] < 0 or new_loc[1] >= 4:
    return None
  return c, new_loc


def get_moves(loc, path):
  moves = []
  h = md5(path)
  if h[0] in OPEN:
    moves.append(get_move(loc, 'U'))
  if h[1] in OPEN:
    moves.append(get_move(loc, 'D'))
  if h[2] in OPEN:
    moves.append(get_move(loc, 'L'))
  if h[3] in OPEN:
    moves.append(get_move(loc, 'R'))
  return filter(lambda x: x is not None, moves)


def dfs(loc, path):
  print(loc)
  if loc == (3, 3):
    return True, path
  moves = get_moves(loc, path)
  for my_dir, new_loc in moves:
    retval, new_path = dfs(new_loc, "%s%s" % (path, my_dir))
    if retval:
      return True, new_path
  return False, ""


def solve1():
  loc = (0, 0)
  solved, path = dfs(loc, problem_input)
  return path


if __name__ == "__main__":
  print(solve1())
