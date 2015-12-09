import re
import string


def solve1(in_file):
    total = 0
    for line in in_file:
        if pred1(line) and pred2(line) and pred3(line):
            total += 1
    return total

def solve2(in_file):
    total = 0
    for line in in_file:
        if pred4(line) and pred5(line):
            total += 1
    return total


def pred1(st):
    return re.search("[aeiou].*[aeiou].*[aeiou]", st)


def pred2(st):
    pat = "aa"
    for elem in string.ascii_lowercase[1:]:
        pat = "%s|%s%s" % (pat, elem, elem)
    return re.search(pat, st)


def pred3(st):
    return not re.search("ab|cd|pq|xy", st)


def pred4(st):
    pat = ""
    for elem1 in string.ascii_lowercase:
        for elem2 in string.ascii_lowercase:
            pat = "%s|%s%s.*%s%s" % (pat, elem1, elem2, elem1, elem2)
    pat = pat[1:]
    return re.search(pat, st)


def pred5(st):
    pat = "a.a"
    for elem in string.ascii_lowercase[1:]:
        pat = "%s|%s.%s" % (pat, elem, elem)
    return re.search(pat, st)


if __name__ == "__main__":
    in_file = [x.strip() for x in open('day5.in').readlines()]
    print(solve1(in_file))
    print(solve2(in_file))
