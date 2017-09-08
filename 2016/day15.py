import re


class Disc(object):
  def __init__(self, mod_value, start):
    self.mod_value = mod_value
    self.start = start

  def is_open(self, time):
    return (self.start + time) % self.mod_value == 0


def disc_from_str(s):
  m = re.match(r".* (\d+) .*(\d+).", s)
  return Disc(int(m.group(1)), int(m.group(2)))


def read_discs(add_extra=False):
  discs = [disc_from_str(x.strip()) for x in open('day15.in').readlines()]
  if add_extra:
    discs.append(Disc(11, 0))
  for i in range(0, len(discs)):
    discs[i].start += i + 1
  return discs


def solve1():
  """
  Brute Force
  :return:
  """
  discs = read_discs()
  time = 0
  while True:
    if all([x.is_open(time) for x in discs]):
      return time
    time += 1

def solve2():
  """
  Brute Force
  :return:
  """
  discs = read_discs(True)
  time = 0
  while True:
    if all([x.is_open(time) for x in discs]):
      return time
    time += 1



if __name__ == "__main__":
  print(solve1())
  print(solve2())
