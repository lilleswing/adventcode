import re
import string

letters = string.ascii_lowercase
letters = letters.replace("i", "")
letters = letters.replace("l", "")
letters = letters.replace("o", "")
lookup1 = {x[0]: x[1] for x in zip(xrange(100), list(letters))}
lookup2 = {x[1]: x[0] for x in zip(xrange(100), list(letters))}


def to_numbers(password):
    return [lookup2[x] for x in password][::-1]


def to_string(numbers):
    return "".join([lookup1[x] for x in numbers][::-1])


def next_password(passwod):
    values = to_numbers(passwod)
    for i in xrange(0, len(values)):
        next_val = values[i] + 1
        if next_val in lookup1:
            values[i] = next_val
            return to_string(values)
        values[i] = 0
    raise Exception()


def is_valid(passwd):
    def pred1(passwd):
        for i in xrange(2, len(passwd)):
            v0 = ord(passwd[i - 2])
            v1 = ord(passwd[i - 1])
            v2 = ord(passwd[i - 0])
            if v0 + 1 == v1 and v1 + 1 == v2:
                return True
        return False

    def pred2(passwd):
        pat = ""
        for elem1 in letters:
            for elem2 in letters:
                pat = "%s|%s%s.*%s%s" % (pat, elem1, elem1, elem2, elem2)
        pat = pat[1:]
        return re.search(pat, passwd)

    return pred1(passwd) and pred2(passwd)


def solve1(password):
    password = next_password(password)
    while not is_valid(password):
        password = next_password(password)
    return password


if __name__ == "__main__":
    print(solve1("vzbxkghb"))
    print(solve1("vzbxxyzz"))
