import re


def solve1(lines):
    def score(st):
        st = st[1:-1]
        p1 = len(re.findall("\\\\x[1234567890abcdef][1234567890abcdef]", st)) * 3
        p2 = len(re.findall("\\\\\"", st))
        p3 = len(re.findall("\\\\\\\\", st))
        my_score = p1 + p2 + p3 + 2
        # print(st, my_score)
        return 2 + p1 + p2 + p3

    total = 0
    for line in lines:
        total += score(line)
    return total


def solve2(lines):
    def score(st):
        st = st[1:-1]
        p1 = len(re.findall("\\\\x[1234567890abcdef][1234567890abcdef]", st))
        p2 = len(re.findall("\\\\\"", st)) * 2
        p3 = len(re.findall("\\\\\\\\", st)) * 2
        return 4 + p1 + p2 + p3

    total = 0
    for line in lines:
        total += score(line)
    return total


if __name__ == "__main__":
    all_lines = [x.strip() for x in open('day8.in').readlines()]
    print(solve1(all_lines))
    print(solve2(all_lines))
