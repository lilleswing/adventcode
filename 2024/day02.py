def is_valid_p1(l):
    l = l.split()
    l = [int(x) for x in l]
    s_l = sorted(l)
    s_l_r = sorted(l, reverse=True)

    is_ordered = l == s_l
    is_ordered_r = l == s_l_r
    is_valid = is_ordered or is_ordered_r
    if not is_valid:
        return False
    for i in range(1, len(l)):
        delta = abs(l[i]-l[i-1])
        if delta < 1:
            return False
        if delta > 3:
            return False
    return True

def is_valid_p2(l):
    s_l = sorted(l)
    s_l_r = sorted(l, reverse=True)

    is_ordered = l == s_l
    is_ordered_r = l == s_l_r
    is_valid = is_ordered or is_ordered_r
    if not is_valid:
        return False
    for i in range(1, len(l)):
        delta = abs(l[i]-l[i-1])
        if delta < 1:
            return False
        if delta > 3:
            return False
    return True


def part1():
    lines = open('day02.in').readlines()
    total = 0
    for x in lines:
        x = x.strip()
        if is_valid_p1(x):
            total += 1
    print(total)

def p2_is_line_valid_combo(line):
    is_valid = is_valid_p2(line)
    if is_valid:
        return True
    for idx in range(len(line)):
        new_line = line[0:idx] + line[idx+1:]
        if is_valid_p2(new_line):
            return True
    return False


def part2():
    lines = open('day02.in').readlines()
    lines = [x.strip() for x in lines]
    lines = [x.split() for x in lines]
    total = 0
    for line in lines:
        line = [int(x) for x in line]
        if p2_is_line_valid_combo(line):
            total += 1
    print(total)

if __name__ == "__main__":
    part1()
    part2()
