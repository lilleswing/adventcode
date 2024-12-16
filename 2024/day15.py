from collections import defaultdict


class Board(object):
    def __init__(self):
        self.board = defaultdict(lambda: '#')
        self.row_len = None
        self.col_len = None
        self.moves = []
        self.cur_step = 0
        self.robot = None

    def load_board(self, lines):
        self.row_len = len(lines)
        self.col_len = len(lines[0])
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                self.board[(i, j)] = c
                if c == '@':
                    self.robot = (i, j)

    def load_moves(self, lines):
        lines = "".join(lines)
        self.moves = lines

    def step(self):
        dirs = {
            'v': (1, 0),
            '^': (-1, 0),
            '>': (0, 1),
            '<': (0, -1)
        }
        move = self.moves[self.cur_step]
        self.cur_step += 1
        self.move(dirs[move])

    def move(self, my_dir):
        r, c = self.robot
        nr, nc = self.robot[0] + my_dir[0], self.robot[1] + my_dir[1]
        if self.board[(nr, nc)] == '#':
            return
        if self.board[(nr, nc)] == 'O':
            self.move_box_stack((nr, nc), my_dir)
        if self.board[(nr, nc)] == '.':
            self.board[(r, c)], self.board[(nr, nc)] = self.board[(nr, nc)], self.board[(r, c)]
            self.robot = (nr, nc)

    def move_box_stack(self, pos, my_dir):
        r, c = pos
        nr, nc = r + my_dir[0], c + my_dir[1]
        if self.board[(nr, nc)] == '#':
            return False
        if self.board[(nr, nc)] == 'O':
            self.move_box_stack((nr, nc), my_dir)
        if self.board[(nr, nc)] == '.':
            self.board[(r, c)], self.board[(nr, nc)] = self.board[(nr, nc)], self.board[(r, c)]

    def gps(self):
        total = 0
        for r in range(self.row_len):
            for c in range(self.col_len):
                if self.board[(r, c)] == 'O':
                    total += 100 * r + c
        return total

    def __str__(self):
        s = ''
        for i in range(self.row_len):
            for j in range(self.col_len):
                s += self.board[(i, j)]
            s += '\n'
        return s


class Board2(object):

    def __init__(self):
        self.board = defaultdict(lambda: '#')
        self.row_len = None
        self.col_len = None
        self.moves = []
        self.cur_step = 0
        self.robot = None

    def load_board(self, lines):
        l = []
        for row in lines:
            new_row = []
            for c in row:
                if c == '#':
                    new_row.append('##')
                elif c == 'O':
                    new_row.append('[]')
                elif c == '.':
                    new_row.append('..')
                elif c == '@':
                    new_row.append('@.')
                else:
                    raise ValueError('Invalid character')
            l.append("".join(new_row))
        lines = l
        print(lines)
        self.row_len = len(lines)
        self.col_len = len(lines[0])
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                self.board[(i, j)] = c
                if c == '@':
                    self.robot = (i, j)

    def load_moves(self, lines):
        lines = "".join(lines)
        self.moves = lines

    def step(self):
        dirs = {
            'v': (1, 0),
            '^': (-1, 0),
            '>': (0, 1),
            '<': (0, -1)
        }
        move = self.moves[self.cur_step]
        self.cur_step += 1
        self.move(dirs[move])

    def move(self, my_dir):
        r, c = self.robot
        nr, nc = self.robot[0] + my_dir[0], self.robot[1] + my_dir[1]
        if self.board[(nr, nc)] == '#':
            return
        if self.board[(nr, nc)] == '[':
            can_move = self.move_box_stack((r, c), my_dir, check_only=True)
            if can_move:
                self.move_box_stack((r, c), my_dir, check_only=False)
                self.robot = (nr, nc)
            return
        if self.board[(nr, nc)] == ']':
            can_move = self.move_box_stack((r, c), my_dir, check_only=True)
            if can_move:
                self.move_box_stack((r, c), my_dir, check_only=False)
                self.robot = (nr, nc)
            return
        if self.board[(nr, nc)] == '.':
            self.board[(r, c)], self.board[(nr, nc)] = self.board[(nr, nc)], self.board[(r, c)]
            self.robot = (nr, nc)
            return

    def move_box_stack(self, pos, my_dir, check_only=False):
        r, c = pos
        nr, nc = r + my_dir[0], c + my_dir[1]
        if self.board[(nr, nc)] == '#':
            return False
        if self.board[(nr, nc)] == '[' and my_dir in [(0, 1), (0, -1)]: # horizontal
            v = self.move_box_stack((nr, nc), my_dir, check_only=check_only)
            if check_only:
                return v
        if self.board[(nr, nc)] == ']' and my_dir in [(0, 1), (0, -1)]: # horizontal
            v = self.move_box_stack((nr, nc), my_dir, check_only=check_only)
            if check_only:
                return v
        if self.board[(nr, nc)] == '[' and my_dir in [(-1, 0), (1, 0)]: # vertical
            v1 = self.move_box_stack((nr, nc), my_dir, check_only=check_only)
            p2 = (nr, nc+1)
            v2 = self.move_box_stack(p2, my_dir, check_only=check_only)
            if check_only:
                return v1 and v2
        if self.board[(nr, nc)] == ']' and my_dir in [(-1, 0), (1, 0)]: # vertical
            v1 = self.move_box_stack((nr, nc), my_dir, check_only=check_only)
            p2 = (nr, nc-1)
            v2 = self.move_box_stack(p2, my_dir, check_only=check_only)
            if check_only:
                return v1 and v2
        if self.board[(nr, nc)] == '.':
            if not check_only:
                self.board[(r, c)], self.board[(nr, nc)] = self.board[(nr, nc)], self.board[(r, c)]
            return True
        raise ValueError("Invalid state")

    def gps(self):
        total = 0
        for r in range(self.row_len):
            for c in range(self.col_len):
                if self.board[(r, c)] == '[':
                    total += 100 * r + c
        return total

    def __str__(self):
        s = ''
        for i in range(self.row_len):
            for j in range(self.col_len):
                s += self.board[(i, j)]
            s += '\n'
        return s


def parse(fname, fn=lambda: Board()):
    with open(fname) as f:
        data = f.read().strip().split('\n')
    data = [x.strip() for x in data]
    idx = 0
    while data[idx] != '':
        idx += 1
    board = fn()
    board.load_board(data[:idx])
    board.load_moves(data[idx + 1:])
    return board


def part1(fname):
    parse(fname)
    board = parse(fname)
    for step in board.moves:
        board.step()
    print(board)
    print(board.gps())


def part2(fname):
    parse(fname)
    board = parse(fname, fn=lambda: Board2())
    for step in board.moves:
        board.step()
    print(board)
    print(board.gps())


if __name__ == "__main__":
    # part1('day15.in')
    part2('day15.in')
