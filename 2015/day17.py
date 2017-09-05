import numpy as np


def solve1(containers, size):
    dp = np.zeros(size + 1)
    dp[0] = 1
    for container in containers:
        additive = np.zeros(size + 1)
        for i in xrange(container, len(dp)):
            additive[i] += dp[i - container]
        dp = dp + additive
    return dp[-1]


def solve2(containers, size):
    dp = np.zeros([len(containers), size + 1])
    dp[0][0] = 1
    for container in containers:
        additive = np.zeros([len(containers), size + 1])
        for r in xrange(len(containers) - 1):
            for c in xrange(size + 1):
                if c - container < 0 or r + 1 > len(containers):
                    continue
                additive[r + 1][c] += dp[r][c - container]
        dp = dp + additive
    solutions = dp[:, -1]
    for solution in solutions:
        if solution == 0:
            continue
        return solution
    raise Exception()


def main():
    containers = [int(x.strip()) for x in open('day15.in').readlines()]
    print(solve1(containers, 150))
    print(solve2(containers, 150))


if __name__ == "__main__":
    main()
