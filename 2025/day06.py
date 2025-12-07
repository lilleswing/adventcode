import pandas as pd
def get_fn(s):
    if s == '+':
        return lambda x, y: int(x)+int(y)
    else:
        return lambda x, y: int(x)*int(y)

def reduce_it(fn, l):
    a = l[0]
    for b in l[1:]:
        a = fn(a, b)
    return a


def part2():
    data = open('day06.in').readlines()
    data = [x.strip('\n') for x in data]
    data, ops = data[:-1], data[-1]
    cutoffs = []
    for idx, c in enumerate(ops):
        if c not in  (' ', '_'):
            cutoffs.append(idx)
    cutoffs.append(len(ops)+1)
    total = 0
    for idx in range(1, len(cutoffs)):
        low, high = cutoffs[idx-1], cutoffs[idx]-1
        fn = get_fn(ops[low])
        nums = []
        for row in data:
            n = row[low:high]
            nums.append(n)
        col_idxs = range(len(nums[0]))[::-1]
        col_nums = []
        for col_idx in col_idxs:
            s = ""
            for num in nums:
                if num[col_idx] in (' ', '_'):
                    continue
                s += num[col_idx]
            col_nums.append(int(s))
        my_part = reduce_it(fn, col_nums)
        print(col_nums, my_part)
        total += my_part
    print(total)


def part1():
    data = open('day06.in').readlines()
    data = [x.strip().split() for x in data]
    data, ops = data[:-1], data[-1]
    total = 0
    for i, op in enumerate(ops):
        fn = get_fn(op)
        l = []
        for row in range(len(data)):
            l.append(data[row][i])
        total += reduce_it(fn, l)
    print(total)



if __name__ == "__main__":
    #part1()
    part2()
