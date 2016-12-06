import hashlib


def hash_str(s):
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()

def is_good_hash(h):
    if h[:5] == "00000":
        return True
    return False

def solve1(start):
    salt = 0
    password = ""
    while len(password) < 8:
        s = "%s%s" % (start, salt)
        h = hash_str(s)
        if is_good_hash(h):
            password += h[5]
        salt += 1
    return password

def solve2(start):
    def get_location(h):
        index = h[5]
        value = h[6]
        try:
            index = float(index)
            if index > 7:
                return -1, '+'
            return index, value
        except:
            return -1, '+'


    password = {}
    salt = 0
    while len(password) < 8:
        s = "%s%s" % (start, salt)
        h = hash_str(s)
        if is_good_hash(h):
            location, value = get_location(h)
            if location >= 0 and location not in password:
                password[location] = value
        salt += 1
    l = sorted([(x,y) for x,y in password.iteritems()])
    return "".join([x[1] for x in l])


def test():
    print(solve1("abc"))
    print(solve2("abc"))


if __name__ == "__main__":
    print(solve1(start = "ffykfhsq"))
    print(solve2(start = "ffykfhsq"))

