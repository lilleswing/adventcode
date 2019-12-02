from aoc2019 import read_file

def parse_input():
    #return [1,0,0,0, 99]
    #return [2,3,0,3,99]
    #return [2, 4, 4, 5, 99, 0]
    l = read_file('day2.in')
    l = [int(x) for x in l[0].split(',')]
    l[1] = 12
    l[2] = 2
    return l


def solve1():
    done = False
    index = 0

    l = parse_input()

    while not done:
        op_code = l[index]
        if op_code == 99:
            done = True
            continue
        if op_code == 1:
            v1 = l[l[index+1]]
            v2 = l[l[index+2]]
            result = v1 + v2
            dest_index = l[index+3]
            l[dest_index] = result
            index += 4
            continue
        if op_code == 2:
            v1 = l[l[index+1]]
            v2 = l[l[index+2]]
            result = v1 * v2
            dest_index = l[index+3]
            l[dest_index] = result
            index += 4
            continue
    return l[0]

def run_round(noun, verb):
    done = False
    index = 0

    l = parse_input()
    l[1] = noun
    l[2] = verb
    while not done:
        op_code = l[index]
        if op_code == 99:
            done = True
            continue
        if op_code == 1:
            v1 = l[l[index+1]]
            v2 = l[l[index+2]]
            result = v1 + v2
            dest_index = l[index+3]
            l[dest_index] = result
            index += 4
            continue
        if op_code == 2:
            v1 = l[l[index+1]]
            v2 = l[l[index+2]]
            result = v1 * v2
            dest_index = l[index+3]
            l[dest_index] = result
            index += 4
            continue
    return l[0]


def solve2_helper(goal):
    for i in range(0, 101):
        for j in range(0, 101):
            if run_round(i, j) == goal:
                return 100*i + j


def solve2():
    goal = 19690720
    return solve2_helper(goal)


def test_solve1():
    assert solve1() == 9581917


def test_solve2():
    assert solve2() == 2505

