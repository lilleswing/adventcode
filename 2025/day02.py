import re

def is_valid_id1(s):
    s = str(s)
    if len(s) % 2 != 0:
        return True
    my_len = len(s)//2
    return s[:my_len] != s[my_len:]

def is_valid_id2(s):
    s = str(s)
    for start in range(1, len(s)//2 + 1):
        p = s[:start]
        p = f"^({p})+$"
        m = re.match(p, s)
        if m is not None:
            return False
    return True



def part1():
    data = open('day02.in').readlines()[0]
    data = data.strip()
    data = data.split(',')
    l = []
    for e in data:
        v1, v2 = e.split('-')
        l.append((int(v1), int(v2)))

    total = 0
    for low, high in l:
        for n in range(low, high+1):
            if not is_valid_id1(n):
                total += n
    print(total)


def part2():
    data = open('day02.in').readlines()[0]
    data = data.strip()
    data = data.split(',')
    l = []
    for e in data:
        v1, v2 = e.split('-')
        l.append((int(v1), int(v2)))

    total = 0
    for low, high in l:
        for n in range(low, high+1):
            if not is_valid_id2(n):
                total += n
    print(total)

if __name__ == "__main__":
    #part1()
    part2()
