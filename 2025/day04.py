def count_neighbors(r,c,board):
    active = 0
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            if dr==0 and dc==0:
                continue
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= len(board):
                continue
            if nc < 0 or nc >=  len(board):
                continue
            if board[nr][nc] == '@':
                active += 1
    return active


def part1():
    lines = open('day04.in').readlines()
    lines = [list(x.strip()) for x in lines]
    total = 0
    bad_spots = []
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] != '@':
                continue
            n = count_neighbors(r,c,lines)
            if n < 4:
                total += 1
                bad_spots.append((r,c))
    for r, c in bad_spots:
        lines[r][c] = 'x'
    for line in lines:
        print("".join(line))
    print(total)

def remove_rolls(lines):
    bad_spots = []
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] != '@':
                continue
            n = count_neighbors(r,c,lines)
            if n < 4:
                bad_spots.append((r,c))
    for r, c in bad_spots:
        lines[r][c] = '.'
    return len(bad_spots)


def part2():
    lines = open('day04.in').readlines()
    lines = [list(x.strip()) for x in lines]
    total = 0
    last_round = -1
    while last_round != 0:
        last_round = remove_rolls(lines)
        total += last_round
    print(total)


if __name__ == "__main__":
    #part1()
    part2()
