import hashlib

input = "yzbqklnj"


def solve2(s):
    done = False
    salt = 1
    while not done:
        md5 = hashlib.md5("%s%s" % (s, salt)).hexdigest()
        if md5[0:6] == '000000':
            return salt
        salt += 1


def solve1(s):
    done = False
    salt = 1
    while not done:
        md5 = hashlib.md5("%s%s" % (s, salt)).hexdigest()
        if md5[0:5] == '00000':
            return salt
        salt += 1


if __name__ == "__main__":
    print(solve1(input))
    print(solve2(input))
