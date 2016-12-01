
def look_and_say(st):
    retval = list()
    stack = list()
    index = -1
    while index < len(st) - 1:
        index += 1
        if len(stack) == 0:
            stack.append(st[index])
            continue
        if st[index] == stack[-1]:
            stack.append(st[index])
            continue
        retval.append("%s%s" % (len(stack), stack[-1]))
        stack = [st[index]]
    retval.append("%s%s" % (len(stack), stack[-1]))
    return "".join(retval)


def solve1(s):
    for i in xrange(40):
        s = look_and_say(s)
    return len(s)

def solve2(s):
    for i in xrange(50):
        s = look_and_say(s)
    return len(s)

if __name__ == "__main__":
    print(solve1("1321131112"))
    print(solve2("1321131112"))
