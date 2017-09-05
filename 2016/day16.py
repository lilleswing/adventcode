initial_state = "10011111011011001"


def swap(s):
  lookup = {
    '0': '1',
    '1': '0'
  }
  return "".join([lookup[x] for x in s])


def solve_helper(length):
  a = initial_state
  while len(a) < length:
    a1 = a
    b = a1[::-1]
    b = swap(b)
    a = "%s0%s" % (a1, b)
  a = a[:length]
  lookup = {
    "00": "1",
    "11": "1",
    "01": "0",
    "10": "0"
  }
  while len(a) % 2 == 0:
    pairs = [a[i:i + 2] for i in range(0, len(a), 2)]
    a = "".join([lookup[x] for x in pairs])
  return a


def solve1():
  return solve_helper(272)


def solve2():
  return solve_helper(35651584)


if __name__ == "__main__":
  print(solve1())
  print(solve2())
