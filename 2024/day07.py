from multiprocessing import Pool
from itertools import product
import tqdm


def parse_line(line):
    line = line.strip()
    line = line.replace(':', '')
    line = line.split(' ')
    line = [int(x) for x in line]
    return line


def is_valid1(goal, nums):
    add = lambda x, y: x + y
    mul = lambda x, y: x * y
    num_ops = len(nums) - 1
    for ops in product([add, mul], repeat=num_ops):
        v = nums[0]
        for e, op in zip(nums[1:], ops):
            v = op(v, e)
        if v == goal:
            return True
    return False


def is_valid2(goal, nums):
    add = lambda x, y: x + y
    mul = lambda x, y: x * y
    cat = lambda x, y: int(str(x)+str(y))

    num_ops = len(nums) - 1
    for ops in product([add, mul, cat], repeat=num_ops):
        v = nums[0]
        for e, op in zip(nums[1:], ops):
            v = op(v, e)
        if v == goal:
            return True
    return False

def is_valid2_unwrapper(args):
    return is_valid2(args[0], args[1]), args[0]


def part1(fname):
    lines = open(fname).readlines()
    lines = [parse_line(x) for x in lines]
    total = 0
    for line in tqdm.tqdm(lines):
        if is_valid1(line[0], line[1:]):
            total += line[0]
    print(total)


def part2(fname):
    lines = open(fname).readlines()
    lines = [parse_line(x) for x in lines]
    total = 0
    with Pool() as pool:
        args = []
        for line in lines:
            args.append((line[0], line[1:]))
        results = pool.imap_unordered(is_valid2_unwrapper, args)
        for works, v in tqdm.tqdm(results, total=len(args)):
            if works:
                total += v

    print(total)

if __name__ == "__main__":
    part1('day07.in')
    part2('day07.in')
