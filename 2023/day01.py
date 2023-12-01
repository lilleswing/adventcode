import re


def part1(fname):
    data = [x.strip() for x in open(fname).readlines()]
    total = 0
    for e in data:
        l = re.findall("\d", e)
        v = int(l[0] + l[-1])
        total += v
    print(total)


def parse_it(s, words):
    l = []
    while len(s) > 0:
        for w, v in words.items():
            if s.startswith(w):
                l.append(str(v))
        s = s[1:]
    return l


def part2(fname):
    data = [x.strip() for x in open(fname).readlines()]
    words = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    for i in range(0, 10):
        words[str(i)] = i

    total = 0
    for e in data:
        l = parse_it(e, words)
        v = int(l[0] + l[-1])
        total += v
    print(total)


if __name__ == "__main__":
    part1('day01.in')
    part2('day01.in')
