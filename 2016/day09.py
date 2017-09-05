import re

pattern = r"(\((\d+)x(\d+)\)).*"


def solve1():
  data = open('day09.in', encoding='UTF-8').read()
  total = 0
  while len(data) > 0:
    m = re.match(pattern, data)
    if m:
      marker, num_c, num_r = m.groups()
      data = data[len(marker) + int(num_c):]
      total += int(num_c) * int(num_r)
      continue
    data = data[1:]
    total += 1
  return total


def decode_str(s):
  total = 0
  while len(s) > 0:
    m = re.match(pattern, s)
    if m:
      marker, num_c, num_r = m.groups()
      num_c, num_r = int(num_c), int(num_r)
      s = s[len(marker):]
      total += num_r * decode_str(s[:num_c])
      s = s[num_c:]
      continue
    s = s[1:]
    total += 1
  return total


def solve2():
  data = open('day09.in', encoding='UTF-8').read()
  return decode_str(data)


if __name__ == "__main__":
  print(solve1())
  print(solve2())
