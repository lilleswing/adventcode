def make_key(x, y):
    return "%s:%s" % (x, y)


def solve2(str):
    houses = set()
    locs = [(0, 0), (0, 0)]
    turn = 0
    for i in xrange(len(str)):
        my_x, my_y = locs[turn]
        houses.add(make_key(my_x, my_y))
        c = str[i]
        if c == '>':
            my_x += 1
        if c == '<':
            my_x -= 1
        if c == '^':
            my_y += 1
        if c == 'v':
            my_y -= 1
        houses.add(make_key(my_x, my_y))
        locs[turn] = (my_x, my_y)
        turn = (turn + 1) % 2
    return len(houses)


def solve1(str):
    houses = set()
    my_x = 0
    my_y = 0
    for i in xrange(len(str)):
        houses.add(make_key(my_x, my_y))
        c = str[i]
        if c == '>':
            my_x += 1
        if c == '<':
            my_x -= 1
        if c == '^':
            my_y += 1
        if c == 'v':
            my_y -= 1
    return len(houses)


if __name__ == "__main__":
    infile = open('day3.in').read().strip()
    print(solve1(infile))
    print(solve2(infile))
