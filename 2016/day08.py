import re

data = [x.strip() for x in open('day08.in').readlines()]


class Board(object):
    def __init__(self):
        l = []
        for i in xrange(6):
            l.append([False] * 50)
        self.board = l

    def move(self, s):
        if s.startswith("rect"):
            self._rect(s)
            return
        if s.startswith("rotate row"):
            self._rotate_row(s)
            return
        if s.startswith("rotate column"):
            self._rotate_col(s)
            return
        raise Exception("Cannot Match")

    def _rect(self, s):
        m = re.search(r"rect (\d+)x(\d+)", s)
        x = int(m.group(1))
        y = int(m.group(2))
        for r in xrange(y):
            for c in xrange(x):
                self.board[r][c] = True

    def _rotate_row(self, s):
        m = re.search(r"rotate row y=(\d+) by (\d+)", s)
        y = int(m.group(1))
        s = int(m.group(2))
        row = self._get_row(y)
        row = self._cycle_list(row, s)
        self._set_row(y, row)

    def _rotate_col(self, s):
        m = re.search(r"rotate column x=(\d+) by (\d+)", s)
        x = int(m.group(1))
        s = int(m.group(2))
        col = self._get_col(x)
        col = self._cycle_list(col, s)
        self._set_col(x, col)

    def _get_row(self, y):
        return self.board[y]

    def _set_row(self, y, row):
        self.board[y] = row

    @staticmethod
    def _cycle_list(row, s):
        l2 = [0] * len(row)
        for i in xrange(len(row)):
            end_index = (i + s) % len(row)
            l2[end_index] = row[i]
        return l2

    def _set_col(self, x, col):
        for i in xrange(len(col)):
            self.board[i][x] = col[i]

    def _get_col(self, x):
        l2 = list()
        for i in xrange(len(self.board)):
            l2.append(self.board[i][x])
        return l2

    def display(self):
        s = ""
        for r in xrange(len(self.board)):
            for c in xrange(len(self.board[0])):
                if self.board[r][c]:
                    s += "#"
                else:
                    s += "-"
            s += "\n"
        return s

    def num_lit(self):
        total = 0
        for r in xrange(len(self.board)):
            for c in xrange(len(self.board[0])):
                if self.board[r][c]:
                    total += 1
        return total


def solve1():
    b = Board()
    for line in data:
        b.move(line)
    return b.num_lit()


def solve2():
    b = Board()
    for line in data:
        b.move(line)
    return b.display()


if __name__ == "__main__":
    print(solve1())
    print(solve2())
