import json


def solve_value(my_part):
    try:
        return int(my_part)
    except ValueError:
        return 0


def solve1(part):
    def solve_dict(my_part):
        total = 0
        for key, value in my_part.iteritems():
            total += solve1(key)
            total += solve1(value)
        return total

    def solve_list(my_part):
        total = 0
        for value in my_part:
            total += solve1(value)
        return total

    if isinstance(part, dict):
        return solve_dict(part)
    if isinstance(part, list):
        return solve_list(part)
    return solve_value(part)


def solve2(part):
    def solve_dict(my_part):
        if "red" in my_part.values():
            return 0
        total = 0
        for key, value in my_part.iteritems():
            total += solve2(key)
            total += solve2(value)
        return total

    def solve_list(my_part):
        total = 0
        for value in my_part:
            total += solve2(value)
        return total

    if isinstance(part, dict):
        return solve_dict(part)
    if isinstance(part, list):
        return solve_list(part)
    return solve_value(part)


if __name__ == "__main__":
    print(solve1(json.loads(open('day12.json').read())))
    print(solve2(json.loads(open('day12.json').read())))
