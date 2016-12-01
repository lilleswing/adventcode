import re


def f1(ingredients, l):
    values = list()
    for i in xrange(1, len(ingredients[0]) - 1):
        value = 0
        for j in xrange(len(ingredients)):
            value += l[j] * ingredients[j][i]
        values.append(value)
    values = [max(0, x) for x in values]
    return reduce(lambda x, y: x * y, values, 1)


def f2(ingredients, l):
    value = 0
    for j in xrange(len(ingredients)):
        value += l[j] * ingredients[j][-1]
    if value != 500:
        return 0
    return f1(ingredients, l)


def solve1(ingredients):
    best = 0
    l = [0] * len(ingredients)
    for i in xrange(0, 100):
        l[0] = i
        for j in xrange(0, 100 - i):
            l[1] = j
            for k in xrange(0, 100 - i - j):
                l[2] = k
                l[3] = 100 - i - j - k
                my_value = f1(ingredients, l)
                if my_value > best:
                    best = my_value
    return best


def solve2(ingredients):
    best = 0
    l = [0] * len(ingredients)
    for i in xrange(0, 100):
        l[0] = i
        for j in xrange(0, 100 - i):
            l[1] = j
            for k in xrange(0, 100 - i - j):
                l[2] = k
                l[3] = 100 - i - j - k
                my_value = f2(ingredients, l)
                if my_value > best:
                    best = my_value
    return best


def parse(lines):
    pattern = "(.+): capacity (.+), durability (.+), flavor (.+), texture (.+), calories (.+)"
    ingredients = list()
    for line in lines:
        match = re.match(pattern, line)
        name = match.group(1)
        capacity = int(match.group(2))
        durability = int(match.group(3))
        flavor = int(match.group(4))
        texture = int(match.group(5))
        calories = int(match.group(6))
        ingredients.append((name, capacity, durability, flavor, texture, calories))
    return ingredients


if __name__ == "__main__":
    my_ingredients = parse([x.strip() for x in open('day15.in').readlines()])
    print(solve1(my_ingredients))
    print(solve2(my_ingredients))
