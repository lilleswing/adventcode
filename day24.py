def solve1():
    """
    Solved looking at the list of numbers and trying the first thing that worked for 1/3
    113,109,107,103,83
    :return:
    """
    pass


min_packages = 100000
solutions = list()


def solve2():
    """
    Didn't actually check through -- simply found the group that equals goal with the lowest QE and assume
    that the other requirements would be satisfied
    """

    def dfs(i, v):
        if v == goal:
            result = filter(lambda x: x[0], zip(lb, values))
            if len(result) == 5:
                solutions.append(result)
            return False
        if i >= len(values) or v > goal:
            return False
        lb[i] = True
        v += values[i]
        retval = dfs(i + 1, v)
        if retval:
            return True
        v -= values[i]
        lb[i] = False
        return dfs(i + 1, v)

    def qe(l):
        prod = 1
        for i in l:
            prod *= i[1]
        return prod

    values = [int(x) for x in open('day24.in').readlines()][::-1]
    lb = [False] * len(values)
    total = sum(values)
    goal = total / 4
    dfs(0, 0)
    my_sols = sorted([qe(x) for x in solutions])
    return my_sols[0]


def main():
    print(solve2())


if __name__ == "__main__":
    main()
