low_area = 197487
high_area = 673251

def has_double(i):
    s = str(i)
    for i in range(2, len(s)+1):
        if len(set(s[i-2:i])) == 1:
            return True
    return False

def monitonically_increasing(i):
    s = str(i)
    l = [int(x) for x in s]
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            return False
    return True
    
def check_number1(i):
    if not has_double(i):
        return False
    if not monitonically_increasing(i):
        return False
    return True

def not_triple(s, i):
    if i >= 2:
        part = s[i-3:i]
        if len(set(list(part))) == 1:
            return False
    if i+1 <= len(s):
        part = s[i-2:i+1]
        if len(set(list(part))) == 1:
            return False
    return True

def has_double_and_not_triple(i):
    s = str(i)
    for i in range(2, len(s)+1):
        if len(set(s[i-2:i])) == 1:
            if not_triple(s, i):
                return True
    return False

def check_number2(i):
    if not has_double_and_not_triple(i):
        return False
    if not monitonically_increasing(i):
        return False
    return True


def solve1():
    total = 0
    for i in range(low_area, high_area):
        total += check_number1(i)
    return total

def solve2():
    total = 0
    for i in range(low_area, high_area):
        total += check_number2(i)
    return total


def test_solve1():
    assert solve1() == 1640
    
    
def test_solve2():
    assert solve2() == 1126