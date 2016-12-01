row, column = 3010, 3019
#row, column = 4, 5


def get_hash_number(r, c):
    value = 1
    additive = 1
    for i in xrange(1, r):
        value += additive
        additive += 1

    col_additive = row + 1
    for i in xrange(1, c):
        value += col_additive
        col_additive += 1
    return value


def solve1():
    def santa_hash(start_val):
        return (start_val * 252533) % 33554393

    num_hashes = get_hash_number(row, column)
    hash_val = 20151125
    for i in xrange(1, num_hashes):
        hash_val = santa_hash(hash_val)
    return hash_val


def main():
    print(solve1())


if __name__ == "__main__":
    main()
