import collections
data = [x.strip() for x in open('day06.in').readlines()]

def solve_helper(f):
    l = []
    for i in xrange(len(data[0])):
        l.append(collections.Counter())
    for line in data:
        for i, c in enumerate(list(line)):
            l[i][c] += 1
    retval = [f(x.iteritems(), key=lambda x: x[1]) for x in l]
    return "".join([x[0] for x in retval])


def solve1():
    return solve_helper(max)


def solve2():
    return solve_helper(min)

if __name__ == "__main__":
    print(solve1())
    print(solve2())
