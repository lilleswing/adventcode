def isint(s):
    try:
        int(s)
        return True
    except:
        return False


def get_num_idx(s):
    retval = []
    state = 'SEARCHING'
    start_idx = None
    end_idx = None
    for i in range(len(s)):
        if isint(s[i]) and state == 'SEARCHING':
            state = 'IN_NUM'
            start_idx = i
        if isint(s[i]) and state == 'IN_NUM':
            continue
        if not isint(s[i]) and state == 'IN_NUM':
            state = 'SEARCHING'
            end_idx = i
            retval.append((start_idx, end_idx))
    if state == 'IN_NUM':
        retval.append((start_idx, len(s)))
    return retval


def is_in_bounds(x, y, engine):
    if y < 0 or y >= len(engine):
        return False
    if x < 0 or x >= len(engine[0]):
        return False
    return True


def is_valid(row, num_idx, engine):
    num_chars = set(list("0123456789"))
    for i in range(num_idx[0], num_idx[1]):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = i + dx, row + dy
                if is_in_bounds(nx, ny, engine):
                    if engine[ny][nx] != '.' and engine[ny][nx] not in num_chars:
                        return True
    return False


def part1(fname):
    engine = [x.strip() for x in open(fname).readlines()]
    total = 0
    for i, row in enumerate(engine):
        nums = get_num_idx(row)
        for n in nums:
            if is_valid(i, n, engine):
                v = int(row[n[0]:n[1]])
                total += v
    print(total)


def check_gear(r, c, engine, idx_dict, idx_to_val):
    nums_around = set()

    for dy in range(-1, 2):
        for dx in range(-1, 2):
            ny, nx = r + dy, c + dx
            if not is_in_bounds(nx, ny, engine):
                continue
            if (ny, nx) in idx_dict:
                nums_around.add(idx_dict[(ny, nx)])
    if len(nums_around) != 2:
        return False, -1, -1

    nums_around = list(nums_around)
    return True, idx_to_val[nums_around[0]], idx_to_val[nums_around[1]]


def part2(fname):
    engine = [x.strip() for x in open(fname).readlines()]
    idx_dict = {}
    idx_to_val = {}
    unique_values = set()
    num_idx = 0
    for i, row in enumerate(engine):
        nums = get_num_idx(row)
        for n in nums:
            value = int(row[n[0]:n[1]])
            unique_values.add(value)
            for x in range(n[0], n[1]):
                idx_dict[(i, x)] = num_idx
            idx_to_val[num_idx] = value
            num_idx += 1

    total = 0
    for r in range(len(engine)):
        for c in range(len(engine)):
            ch = engine[r][c]
            if ch == '*':
                is_gear, v1, v2 = check_gear(r, c, engine, idx_dict, idx_to_val)
                if is_gear:
                    total += v1 * v2
    print(total)


if __name__ == "__main__":
    part1('day03.in')
    part2('day03.in')
