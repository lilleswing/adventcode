def solve2(lines):
    total = 0
    for line in lines:
        vars = [int(k) for k in line.split('x')]
        smallest = smallest_two(vars)
        for small in smallest:
            total += 2 * small
        total += vars[0] * vars[1] * vars[2]
    return total


def solve1(lines):
    total = 0
    for line in lines:
        vars = [int(k) for k in line.split('x')]
        sides = get_sides(vars)
        for side in sides:
            total += 2 * side
        total += min(sides)
    return total


def smallest_two(vars):
    my_vars = zip(range(len(vars)), vars)
    biggest = max(my_vars, key=lambda x: x[1])
    return [y[1] for y in filter(lambda x: x[0] != biggest[0], my_vars)]


def get_sides(var):
    return var[0] * var[1], var[0] * var[2], var[1] * var[2]


if __name__ == "__main__":
    lines = [x.strip() for x in open('day2.in').readlines()]
    print(solve1(lines))
    print(solve2(lines))
