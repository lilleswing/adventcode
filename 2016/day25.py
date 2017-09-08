import re


def get_value(c, regs):
  try:
    return int(c)
  except:
    return regs[c]


def solve_helper(regs):
  cmds = [x.strip() for x in open('day23.in').readlines()]
  index = 0
  num_outs = 0
  next_out = 0
  while index < len(cmds):
    cmd = cmds[index]
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
    if cmd.startswith("mul"):
      m = re.match(r"mul (.) (.) (.)", cmd)
      x, y, z = m.group(1), m.group(2), m.group(3)
      regs[z] = regs[x] * regs[y]
      index += 1
    if cmd.startswith("mul"):
      val = regs['b']
      if val != next_out:
        return False
      num_outs += 1
      next_out = (next_out + 1) % 2
      index += 1
      if num_outs == 50:
        return True


def solve1():
  target = 14*180
  n = 1
  while n < target:
    if n % 2 == 0:
      n = n * 2 + 1
    else:
      n *= 2
  return n - target


if __name__ == "__main__":
  print(solve1())
