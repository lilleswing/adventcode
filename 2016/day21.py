import collections

import re
from itertools import permutations


def swap_pos(pwd, x, y):
  l = list(pwd)
  l[x], l[y] = l[y], l[x]
  return ''.join(l)


def swap_letter(pwd, x, y):
  l = list(pwd)
  for i, c in enumerate(l):
    if c == x:
      l[i] = y
    if c == y:
      l[i] = x
  return "".join(l)


def rotate_dir(pwd, direction, x):
  l = list(pwd)
  if direction == "left":
    l = l[::-1]
  l = collections.deque(l)
  l.rotate(x)
  l = list(l)
  if direction == 'left':
    l = l[::-1]
  return "".join(l)


def rotate_letter(pwd, x):
  index = pwd.index(x)
  l = collections.deque(list(pwd))
  rots = 1 + index
  if index >= 4:
    rots += 1
  l.rotate(rots)
  return "".join(l)


def reverse(pwd, x, y):
  l = list(pwd)
  elems = l[x:y + 1]
  elems = elems[::-1]
  l[x:y + 1] = elems
  return "".join(l)


def move(pwd, x, y):
  l = list(pwd)
  c = l[x]
  del l[x]
  l.insert(y, c)
  return "".join(l)


def get_instructions():
  return "abcdefgh", [x.strip() for x in open('day21.in').readlines()]

  # start_pwd = "abcde"
  # return start_pwd, [x.strip() for x in open('day21.sample').readlines()]


def solve_helper(pwd, instructions):
  for instruction in instructions:
    # print(pwd)
    m = re.match(r"swap position (\d+) with position (\d+)", instruction)
    if m:
      pwd = swap_pos(pwd, int(m.group(1)), int(m.group(2)))
    m = re.match(r"swap letter (.) with letter (.)", instruction)
    if m:
      pwd = swap_letter(pwd, m.group(1), m.group(2))
    m = re.match(r"rotate (.+) (\d+) .*", instruction)
    if m:
      pwd = rotate_dir(pwd, m.group(1), int(m.group(2)))
    m = re.match(r"rotate based on position of letter (.)", instruction)
    if m:
      pwd = rotate_letter(pwd, m.group(1))
    m = re.match(r"reverse positions (\d+) through (\d+)", instruction)
    if m:
      pwd = reverse(pwd, int(m.group(1)), int(m.group(2)))
    m = re.match(r"move position (\d+) to position (\d+)", instruction)
    if m:
      pwd = move(pwd, int(m.group(1)), int(m.group(2)))
  return pwd


def solve1():
  pwd, instructions = get_instructions()
  return solve_helper(pwd, instructions)


def solve2():
  pwd, instructions = get_instructions()
  scrambled = 'fbgdceah'
  for s in [''.join(x) for x in permutations(scrambled)]:
    if solve_helper(s, instructions) == scrambled:
      return s


if __name__ == "__main__":
  print(solve1())
  print(solve2())
