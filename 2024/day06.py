dirs = [
        (-1,0),
        (0,1),
        (1,0),
        (0,-1)
]

def on_board(board, guard_pos):
    r,c = guard_pos
    if r < 0 or r >= len(board):
        return False
    if c < 0 or c >= len(board[0]):
        return False
    return True


def move(board, guard_pos, guard_dir_idx):
    guard_dir = dirs[guard_dir_idx]
    new_pos = guard_pos[0]+guard_dir[0], guard_pos[1] + guard_dir[1]
    if not on_board(board, new_pos):
        return new_pos, guard_dir_idx

    if board[new_pos[0]][new_pos[1]] != '#':
        return new_pos, guard_dir_idx
    else:
        return guard_pos, (guard_dir_idx+1) % len(dirs)

def get_starting_pos(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == '^':
                return (r,c), 0
    raise ValueError("no guard")


def part1(fname):
    lines = open(fname).readlines()
    board = [x.strip() for x in lines]
    guard_pos, guard_dir_idx = get_starting_pos(board)

    used = set([guard_pos])
    while on_board(board, guard_pos):
        guard_pos, guard_dir_idx = move(board, guard_pos, guard_dir_idx)
        used.add(guard_pos)
    print(len(used)-1)
    return used

def is_loop(board, guard_pos, p):
    if not on_board(board, p):
        return False
    r,c = p
    dir_idx = 0
    board[r][c] = '#'
    used = set()
    key = (guard_pos, dir_idx)
    while key not in used:
        used.add(key)
        guard_pos, dir_idx = move(board, guard_pos, dir_idx)
        if not on_board(board, guard_pos):
            board[r][c] = '.'
            return False
        key = (guard_pos, dir_idx)
    board[r][c] = '.'
    return True


def part2(fname):
    possible = part1(fname)
    lines = open(fname).readlines()
    board = [x.strip() for x in lines]
    board = [list(x) for x in lines]
    guard_pos, guard_dir_idx = get_starting_pos(board)

    possible.remove(guard_pos)
    total = 0
    for p in possible:
        if is_loop(board, guard_pos, p):
            total += 1
    print(total)



if __name__ == "__main__":
    #part1('day06.in')
    part2('day06.in')
