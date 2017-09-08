def read_ranges():
  lines = [[int(y) for y in x.strip().split('-')] for x in open('day20.in').readlines()]
  lines = sorted(lines, key=lambda x: x[0])
  return lines


def solve2():
  lines = read_ranges()
  highest = lines[0][1]
  index = 1
  total = 0
  while index < len(lines):
    if lines[index][0] <= highest + 1:
      if lines[index][1] > highest:
        highest = lines[index][1]
    else:
      total += lines[index][0] - highest - 1
      highest = lines[index][1]
    index += 1
  return total


def solve1():
  lines = read_ranges()
  highest = lines[0][1]
  index = 1
  while lines[index][0] <= highest + 1:
    if lines[index][1] > highest:
      highest = lines[index][1]
    index += 1
  return highest + 1


if __name__ == "__main__":
  print(solve1())
  print(solve2())
