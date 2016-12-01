size = 36000000

def solve1():
    sieve = [10] * (size / 10)
    for i in xrange(2, len(sieve)):
        print(i)
        index = i
        while index < len(sieve):
            sieve[index] += i * 10
            index += i
    for i in xrange(len(sieve)):
        if sieve[i] > size:
            return i
    raise Exception()

def solve2():
    sieve = [11] * (size / 10)
    for i in xrange(2, len(sieve)):
        index = i
        for j in xrange(50):
            if index >= len(sieve):
                break
            sieve[index] += i * 11
            index += i
    for i in xrange(len(sieve)):
        if sieve[i] > size:
            return i
    raise Exception()

def main():
    print(solve1())
    print(solve2())






if __name__ == "__main__":
    main()