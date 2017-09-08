import re


def get_value(c, regs):
  try:
    return int(c)
  except:
    return regs[c]


def solve_helper(regs):
  cmds = [x.strip() for x in open('day12.in').readlines()]
  index = 0
  while index < len(cmds):
    cmd = cmds[index]
    if cmd.startswith('cpy'):
      m = re.match(r"cpy (.+) (.)", cmd)
      val, reg = get_value(m.group(1), regs), m.group(2)
      regs[reg] = val
      index += 1
      continue
    if cmd.startswith("inc"):
      m = re.match(r"inc (.)", cmd)
      regs[m.group(1)] += 1
      index += 1
      continue
    if cmd.startswith("dec"):
      m = re.match(r"dec (.)", cmd)
      regs[m.group(1)] -= 1
      index += 1
      continue
    if cmd.startswith("jnz"):
      m = re.match(r"jnz (.) (\-?\d+)", cmd)
      reg, val = m.group(1), int(m.group(2))
      if get_value(reg, regs) == 0:
        index += 1
      else:
        index += val
      continue
  return regs['a']


def solve1():
  regs = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0
  }
  return solve_helper(regs)


def solve2():
  regs = {
    "a": 0,
    "b": 0,
    "c": 1,
    "d": 0
  }
  return solve_helper(regs)


if __name__ == "__main__":
  print(solve1())
  print(solve2())
