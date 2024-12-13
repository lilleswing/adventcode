import re
import numpy as np


class Eqs(object):
    def __init__(self, r1, c1, r2, c2, r3, c3, part2=False):
        self.r1 = int(r1)
        self.c1 = int(c1)
        self.r2 = int(r2)
        self.c2 = int(c2)
        self.r3 = int(r3)
        self.c3 = int(c3)
        if part2:
            self.r3 += 10000000000000
            self.c3 += 10000000000000

    def solve(self):
        """
        :return:
        return i, j where i * r1 + j * r2 = r3 and i * c1 + j * c2 = c3
        """
        a = np.array([[self.r1, self.r2], [self.c1, self.c2]])
        b = np.array([self.r3, self.c3])
        x = np.linalg.solve(a, b)
        b1, b2 = round(x[0]), round(x[1])
        return b1, b2

    def double_check(self, b1, b2):
        return b1 * self.r1 + b2 * self.r2 == self.r3 and b1 * self.c1 + b2 * self.c2 == self.c3

    def cost(self):
        b1, b2 = self.solve()
        if not self.double_check(b1, b2):
            return 0
        return 3 * b1 + b2

    def __str__(self):
        return f'{self.r1} {self.c1} {self.r2} {self.c2} {self.r3} {self.c3}'


def parse(fname, part2=False):
    lines = open(fname).readlines()
    lines = [x.strip() for x in lines]
    idx = 0
    retval = []
    while idx < len(lines):
        l1, l2, l3 = lines[idx:idx + 3]
        r1, c1 = re.findall(r'(\d+)', l1)
        r2, c2 = re.findall(r'(\d+)', l2)
        r3, c3 = re.findall(r'(\d+)', l3)
        eq = Eqs(r1, c1, r2, c2, r3, c3, part2=part2)
        retval.append(eq)
        idx += 4
    return retval


def part1(fname):
    eqs = parse(fname)
    total = 0
    for eq in eqs:
        total += eq.cost()
    print(total)


def part2(fname):
    eqs = parse(fname, part2=True)
    total = 0
    for eq in eqs:
        total += eq.cost()
    print(total)


if __name__ == "__main__":
    part1('day13.in')
    part2('day13.in')
