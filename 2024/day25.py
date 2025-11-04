import numpy as np

class Piece(object):
    def __init__(self, is_key, counts):
        self.is_key = is_key
        self.counts = counts - 1

    def __repr__(self):
        return f"{self.is_key} {self.counts}"

    def fits(self, other):
        l = self.counts + other.counts
        return np.all(l < 6)

def part1():
    lines = [x.strip() for x in open('day25.in').readlines()]
    pieces = []
    while len(lines) > 0:
        block = lines[:8]
        if lines[0] == "#####":
            is_key = False
        else:
            is_key = True
        block = block[:7]
        block = [list(x) for x in block]
        block = np.array(block)
        # count the number of '#' in each column
        counts = np.sum(block == '#', axis=0)
        p = Piece(is_key, counts)
        # print(block)
        # print(p)
        pieces.append(p)
        lines = lines[8:]


    keys = [x for x in pieces if x.is_key]
    locks = [x for x in pieces if not x.is_key]
    total = 0
    for k in keys:
        for l in locks:
            if k.fits(l):
                total += 1
    print(total)


if __name__ == '__main__':
    part1()