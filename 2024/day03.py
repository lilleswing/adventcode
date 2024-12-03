import re

def get_score(line):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    retval = re.findall(pattern, line)
    total = 0
    for r in retval:
        pat2 = r".+\((\d{1,3}?),(\d{1,3})\)"
        v1, v2 = re.match(pat2, r).groups()
        print(v1,v2)
        total += int(v1) * int(v2)
    return total


def part1():
    lines = open('day03.in').readlines()
    lines = [x.strip() for x in lines]
    total = 0
    for line in lines:
        total += get_score(line)
    print(total)

def flatten(t):
    if t[0] != '':
        return t[0]
    if t[1] != '':
        return t[1]
    return t[2]

def parse_mul(s):
    pat2 = r".+\((\d{1,3}?),(\d{1,3})\)"
    v1, v2 = re.match(pat2, s).groups()
    return int(v1) * int(v2)

def part2():
    lines = open('day03.in').readlines()
    lines = [x.strip() for x in lines]
    lines = "".join(lines)
    p1 = r"mul\(\d{1,3},\d{1,3}\)"
    p2 = r"do\(\)"
    p3 = r"don't\(\)"
    pattern = f"({p1})|({p2})|({p3})"
    total = 0
    retval = re.findall(pattern, lines)
    retval = [flatten(x) for x in retval]
    is_adding = True
    total = 0
    for v in retval:
        if v == "don't()":
            is_adding = False
            continue
        if v == 'do()':
            is_adding = True
            continue
        if not is_adding:
            continue
        total += parse_mul(v)
    print(total)



if __name__ == "__main__":
    #part1()
    part2()
