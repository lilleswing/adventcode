from collections import defaultdict
def get_max_joltage(s):
    my_max = 0
    s = [int(x) for x in list(s)]
    for i in range(0, len(s)):
        for j in range(i+1, len(s)):
            n = int(f"{s[i]}{s[j]}")
            if n > my_max:
                my_max = n
    return my_max

def joltage_dp(s):
    dp = defaultdict(int) # (Number of batteries, Index) = joltage
    for i in range(len(s)):
        cur_bat = int(s[i])
        for n_bat in range(1, 13):
            key = (n_bat, i)
            v1 = dp[(n_bat, i-1)]
            v2 = dp[(n_bat-1, i-1)]* 10 + cur_bat
            dp[key] = max(v1, v2)
    return dp[(12, len(s)-1)]



def part1():
    data = open('day03.in').readlines()
    total = 0
    for row in data:
        v = get_max_joltage(row.strip())
        print(v)
        total += v
    print(total)

def part2():
    data = open('day03.in').readlines()
    total = 0
    for row in data:
        v = joltage_dp(row.strip())
        print(v)
        total += v
    print(total)



if __name__ == "__main__":
    #part1()
    part2()
