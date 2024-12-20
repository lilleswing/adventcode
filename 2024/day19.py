from functools import lru_cache


@lru_cache(maxsize=None)
def dfs(to_match: str, patterns: tuple) -> int:
    if len(to_match) == 0:
        return 1
    total = 0
    for p in patterns:
        if to_match.startswith(p):
            total += dfs(to_match[len(p):], patterns)
    return total


def part1(fname: str) -> None:
    lines = [x.strip() for x in open(fname).readlines()]
    patterns = tuple(lines[0].split(', '))
    to_match = lines[2:]
    total = 0
    for m in to_match:
        v = dfs(m, patterns)
        if v > 0:
            total += 1
    print(f"number of matches {total}")


def part2(fname: str) -> None:
    lines = [x.strip() for x in open(fname).readlines()]
    patterns = tuple(lines[0].split(', '))
    to_match = lines[2:]
    total = 0
    for m in to_match:
        v = dfs(m, patterns)
        total += v
    print(f"number of matches {total}")


if __name__ == "__main__":
    # part1('day19.in')
    part2('day19.in')
