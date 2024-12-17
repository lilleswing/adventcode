from collections import deque

directions = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1)
}


def move(p, board):
    r, c, d = p
    if board[r][c] in ('\\', '/', '|', '-'):  # handle changing direction
        if board[r][c] == '-':
            if d in ('N', 'S'):
                return [(r, c, 'E'), (r, c, 'W')]
            else:
                return [(r + directions[d][0], c + directions[d][1], d)]
        if board[r][c] == '|':
            if d in ('E', 'W'):
                return [(r, c, 'N'), (r, c, 'S')]
            else:
                return [(r + directions[d][0], c + directions[d][1], d)]
        if board[r][c] == '\\':
            if d == 'E':
                return [(r + 1, c, 'S')]
            if d == 'S':
                return [(r, c + 1, 'E')]
            if d == 'N':
                return [(r, c - 1, 'W')]
            if d == 'W':
                return [(r - 1, c, 'N')]
        if board[r][c] == '/':
            if d == 'E':
                return [(r - 1, c, 'N')]
            if d == 'S':
                return [(r, c - 1, 'W')]
            if d == 'N':
                return [(r, c + 1, 'E')]
            if d == 'W':
                return [(r + 1, c, 'S')]
    nr, nc = r + directions[d][0], c + directions[d][1]
    if nr < 0 or nr >= len(board) or nc < 0 or nc >= len(board[0]):
        return []
    return [(nr, nc, d)]


def bounds_check(board, r, c):
    return r >= 0 and r < len(board) and c >= 0 and c < len(board[0])


def solve_configuration(board, start):
    q = deque()
    q.append(start)
    used = set()
    used.add(start)

    while len(q) > 0:
        p = q.pop()
        r, c, _ = p
        if not bounds_check(board, r, c):
            continue
        new_states = move(p, board)
        for s in new_states:
            if s in used:
                continue
            if bounds_check(board, s[0], s[1]):
                used.add(s)
                q.append(s)

    used_spaces = set()
    for e in used:
        used_spaces.add((e[0], e[1]))
    return len(used_spaces)


def part1(fname):
    lines = open(fname).readlines()
    lines = [list(x.strip()) for x in lines]
    retval = solve_configuration(lines, (0, 0, 'E'))
    print(retval)


def part2(fname):
    lines = open(fname).readlines()
    lines = [list(x.strip()) for x in lines]

    activated = []
    for r in range(len(lines)):
        active = solve_configuration(lines, (r, 0, 'E'))
        activated.append(active)

        active = solve_configuration(lines, (r, len(lines[0]) - 1, 'W'))
        activated.append(active)

    for c in range(len(lines[0])):
        active = solve_configuration(lines, (0, c, 'S'))
        activated.append(active)

        active = solve_configuration(lines, (len(lines) - 1, c, 'N'))
        activated.append(active)
    print(max(activated))


if __name__ == "__main__":
    # part1('day16.in')
    part2('day16.in')
