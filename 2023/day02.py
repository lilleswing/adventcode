import re


def parse(s):
    s = s.split(':')[1].strip()
    v = s.split(';')
    retval = []
    for e in v:
        game = {}
        parts = e.split(',')
        for part in parts:
            part = part.strip()
            matches = re.match("(\d+) (.+)", part).groups()
            game[matches[1]] = int(matches[0])
        retval.append(game)
    return retval


def part1(fname):
    lines = [x.strip() for x in open(fname).readlines()]
    games = [parse(x) for x in lines]
    bag_stack = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    total = 0
    for idx, game in enumerate(games):
        game_num = idx + 1
        game_pass = True
        for my_round in game:
            for k, v in my_round.items():
                if v > bag_stack[k]:
                    game_pass = False
        if game_pass:
            total += game_num
    print(total)


def get_min_set(game):
    d = {}
    for my_round in game:
        for k, v in my_round.items():
            if k not in d:
                d[k] = 0
            d[k] = max(d[k], v)
    return d


def power(min_set):
    product = 1
    for k, v in min_set.items():
        product *= v
    return product


def part2(fname):
    lines = [x.strip() for x in open(fname).readlines()]
    games = [parse(x) for x in lines]
    total = 0
    for game in games:
        min_set = get_min_set(game)
        my_power = power(min_set)
        total += my_power
    print(total)


if __name__ == "__main__":
    part1('day02.in')
    part2('day02.in')
