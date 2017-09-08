import re


def get_value(c, regs):
  try:
    return int(c)
  except:
    return regs[c]


def tgl(index, cmds):
  if index >= len(cmds) or index < 0:
    return
  cmd = cmds[index]
  if cmd.startswith("inc"):
    cmds[index] = cmd.replace('inc', 'dec')
  if cmd.startswith("dec"):
    cmds[index] = cmd.replace('dec', 'inc')
  if cmd.startswith("jnz"):
    cmds[index] = cmd.replace('jnz', 'cpy')
  if cmd.startswith('cpy'):
    cmds[index] = cmd.replace('cpy', 'jnz')
  if cmd.startswith('tgl'):
    cmds[index] = cmd.replace('tgl', 'inc')


def solve_helper(regs):
  cmds = [x.strip() for x in open('day23.in').readlines()]
  index = 0
  while index < len(cmds):
    cmd = cmds[index]
    print(index, cmd, regs)
    if cmd.startswith('cpy'):
      m = re.match(r"cpy (.+) (.)", cmd)
      val, reg = get_value(m.group(1), regs), m.group(2)
      try:
        regs[reg] = val
      except:
        print("illegal cpy command")
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
      m = re.match(r"jnz (.) (.+)", cmd)
      reg, val = m.group(1), m.group(2)
      if get_value(reg, regs) == 0:
        index += 1
      else:
        index += get_value(val, regs)
      continue
    if cmd.startswith("tgl"):
      m = re.match(r"tgl (.)", cmd)
      offset = get_value(m.group(1), regs)
      tgl(index + offset, cmds)
      index += 1
    if cmd.startswith("mul"):
      m = re.match(r"mul (.) (.) (.)", cmd)
      x, y, z = m.group(1), m.group(2), m.group(3)
      regs[z] = regs[x] * regs[y]
      index += 1
  return regs['a']


def solve1():
  regs = {
    "a": 7,
    "b": 0,
    "c": 0,
    "d": 0
  }
  return solve_helper(regs)

def solve2():
  regs = {
    "a": 12,
    "b": 0,
    "c": 0,
    "d": 0
  }
  return solve_helper(regs)

if __name__ == "__main__":
  # print(solve1())
  print(solve2())
