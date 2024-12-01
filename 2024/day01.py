from collections import defaultdict

def part2():
    lines = open('day01.in').readlines()
    lines = [x.strip().split() for x in lines]
    lines = [[int(x[0]), int(x[1])] for x in lines]
    v1s = [x[0] for x in lines]
    v2s = [x[1] for x in lines]
    v1s = sorted(v1s)
    v2s = sorted(v2s)

    c = defaultdict(int)
    for v in v2s:
        c[v] += 1

    total = 0
    for v in v1s:
        total += c[v]*v
    print(total)


def part1():
    lines = open('day01.in').readlines()
    lines = [x.strip().split() for x in lines]
    lines = [[int(x[0]), int(x[1])] for x in lines]
    v1s = [x[0] for x in lines]
    v2s = [x[1] for x in lines]
    v1s = sorted(v1s)
    v2s = sorted(v2s)

    total = 0
    for a,b in zip(v1s, v2s):
        total += abs(a-b)
    print(total)

if __name__ == "__main__":
    part1()
    part2()
