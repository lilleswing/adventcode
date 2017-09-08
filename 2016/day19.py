import collections

inp = 3018458


# inp = 5


class Node:
  def __init__(self):
    self.head = None
    self.curr = None
    self.tail = None


def solve1():
  elves = []
  for i in range(1, inp + 1):
    elve = Node()
    elve.curr = i
    elves.append(elve)
  for i in range(1, inp - 1):
    elves[i].head = elves[i - 1]
    elves[i].tail = elves[i + 1]
  elves[0].head = elves[-1]
  elves[0].tail = elves[1]
  elves[-1].head = elves[-2]
  elves[-1].tail = elves[0]
  n_elves = inp
  elf_turn = elves[0]
  while n_elves > 1:
    elf_turn.tail = elf_turn.tail.tail
    elf_turn = elf_turn.tail
    n_elves -= 1
  return elf_turn.curr


def solve2():
  elves = list(range(1, inp + 1))
  index = 0
  while len(elves) > 1:
    if len(elves) % 100 == 0:
      print(len(elves))
    accross = len(elves) // 2
    dead = (index + accross) % len(elves)
    del elves[dead]
    if dead > index:
      index += 1
      index = index % len(elves)
  return elves[0]

def solve_parttwo():
  left = collections.deque()
  right = collections.deque()
  for i in range(1, inp+1):
    if i < (inp// 2) + 1:
      left.append(i)
    else:
      right.appendleft(i)

  while left and right:
    if len(left) > len(right):
      left.pop()
    else:
      right.pop()

    # rotate
    right.appendleft(left.popleft())
    left.append(right.pop())
  return left[0] or right[0]


if __name__ == "__main__":
  # print(solve1())
  print(solve_parttwo())
