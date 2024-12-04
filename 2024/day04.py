def get_dirs():
    for dx in [-1,0,1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            yield (dx, dy)

def bounds_check(positions, board):
    for c, r in positions:
        if c < 0 or c >= len(board):
            return False
        if r < 0 or r >= len(board[0]):
            return False
    return True

def check1(x, y, dx, dy, board):
    positions = [(x,y)]
    for i in range(3):
        new_pos = positions[-1][0]+dx, positions[-1][1]+dy
        positions.append(new_pos)
    if not bounds_check(positions, board):
        return False
    word = []
    for p in positions:
        word.append(board[p[1]][p[0]])
    word = "".join(word)
    print(word)
    if word == 'XMAS' or word == 'SAMX':
        return True
    return False

def part1():
    lines = open('day04.in').readlines()
    lines = [x.strip() for x in lines]
    # go through every starting position and every direction and see if it matches
    total = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            for dx, dy in get_dirs():
                if check1(x, y, dx, dy, lines):
                    total += 1
    print(total/2)
    return total/2

def check_diag(ps, board):
    # letters on d1 and d2 should be [S, M]
    valid = set(['S', 'M'])
    if not bounds_check(ps, board):
        return False
    c1, c2 = [board[ny][nx] for nx, ny in ps]
    if set([c1,c2]) != valid:
        return False
    return True


def check2(x, y, board):
    if board[y][x] != 'A':
        return False
    d1 = [(-1, -1), (1, 1)]
    d2 = [(1, -1), (-1, 1)]

    ps = [(x+dx,y+dy) for dx, dy in d1]
    if not check_diag(ps, board):
        return False
    ps = [(x+dx,y+dy) for dx, dy in d2]
    if not check_diag(ps, board):
        return False
    return True

def part2():
    lines = open('day04.in').readlines()
    lines = [x.strip() for x in lines]

    total = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if check2(x, y, lines):
                total += 1
    print(total)
    return total

if __name__ == "__main__":
    #part1()
    part2()
