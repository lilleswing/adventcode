from collections import deque

def turn_left(q: deque, n:int) -> int:
    total = 0
    for i in range(n):
        v = q.pop()
        q.appendleft(v)
        if q[0] == 0:
            total += 1
    return total

def turn_right(q: deque, n: int) -> int:
    total = 0
    for i in range(n):
        v = q.popleft()
        q.append(v)
        if q[0] == 0:
            total += 1
    return total


def part2():
    lines = open('day01.in').readlines()
    turns = []
    for line in lines:
        direction = line[0]
        value = int(line[1:])
        turns.append((direction, value))

    total = 0
    q = deque()
    for i in range(100):
        q.append(i)
    turn_left(q, 50)
    assert q[0] == 50

    for d, v in turns:
        if d == 'L':
            total += turn_left(q, v)
        else:
            total += turn_right(q, v)
    print(total)


def part1():
    lines = open('day01.in').readlines()
    turns = []
    for line in lines:
        direction = line[0]
        value = int(line[1:])
        turns.append((direction, value))

    total = 0
    starting_point = 50
    for d, v in turns:
        if d == 'L':
            mul = -1
        else:
            mul = 1
        if starting_point == 0:
            total += 1
        starting_point += mul * v
        starting_point += 100
        starting_point = starting_point % 100
    print(total)

if __name__ == "__main__":
    part1()
    part2()
