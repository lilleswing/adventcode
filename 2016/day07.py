import re
import string

data = [x.strip() for x in open('day07.in').readlines()]

def my_split(line):
        return re.split(r"\[|\]", line)

def solve1():
    lines = [my_split(x) for x in data]

    def has_dup(seq):
        for i in xrange(4, len(seq)+1):
            p1 = seq[i-4:i-2]
            p2 = seq[i-2:i][::-1]
            if p1 == p2 and p1[0] != p1[1]:
                return True
        return False

    total = 0
    for line in lines:
        works = False
        for i, part in enumerate(line):
            dup = has_dup(part)
            if i % 2 == 0 and dup:
                works = True
            if i % 2 == 1 and dup:
                works = False
                break
        if works:
            total += 1
    return total

def solve2():
    lines = [my_split(x) for x in data]
    lower = string.ascii_lowercase
    patterns = []
    for c1 in list(lower):
        for c2 in list(lower):
            if c1 == c2:
                continue
            patterns.append("%s%s%s" % (c1,c2,c1))

    def get_triples(part):
        matches = []
        for pat in patterns:
            if part.find(pat) >= 0:
                matches.append(pat)
        return matches

    def reverse_match(match):
        return "".join([match[1],match[0],match[1]])

    total = 0
    for line in lines:
        even_matches = []
        odd_matches = []
        for i, part in enumerate(line):
            if i % 2 == 0:
                even_matches.extend(get_triples(part))
            if i % 2 == 1:
                odd_matches.extend(get_triples(part))
        inverse_odd = [reverse_match(x) for x in odd_matches]
        works = any([x in even_matches for x in inverse_odd])
        if works:
            total += 1
    return total


def test():
    while len(data) > 0:
        data.pop()
    data.append('abba[mnop]qrst')
    data.append('abcd[bddb]xyyx')
    data.append('aaaa[qwer]tyui')
    data.append('ioxxoj[asdfgh]zxcvbn')
    solve1()


if __name__ == "__main__":
    print(solve1())
    print(solve2())
