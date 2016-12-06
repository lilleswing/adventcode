import collections
import string
data = [x.strip() for x in open('day04.in').readlines()]

def parse_id_code(part):
    id_code, checksum = part.split('[')
    id_code = int(id_code)
    checksum = checksum.rstrip(']')
    return id_code, checksum


def is_real(room):
    room = room.split('-')
    cnt = collections.Counter()
    st = "".join(room[:-1])
    for c in st:
        cnt[c] += 1
    l = sorted([(y,x) for x,y in cnt.iteritems()], key=lambda x: x[1])
    l = sorted(l, key=lambda x: x[0], reverse=True)
    calc_checksum = "".join([y[1] for y in l[:5]])

    id_code, checksum = parse_id_code(room[-1])

    if checksum == calc_checksum:
        return True, id_code
    return False, id_code


def solve1():
    total = 0;
    for room in data:
        valid, id_code = is_real(room)
        if valid:
            total += id_code
    return total

to_num = {x:y for x,y in zip(list(string.ascii_lowercase), range(26))}
to_chr = {y:x for x,y in to_num.iteritems()}

def shift(part, id_code):
    nums = [to_num[x] for x in list(part)]
    mod_nums = [(x+id_code) % 26 for x in nums]
    word = [to_chr[x] for x in mod_nums]
    return "".join(word)


def real_name(room):
    room = room.split('-')
    room_name = room[:-1]
    id_code, checksum = parse_id_code(room[-1])
    return " ".join([shift(x, id_code) for x in room_name]), id_code


def solve2():
    real_rooms = filter(lambda x: is_real(x), data)
    l = []
    for room in real_rooms:
        l.append(real_name(room))
    return(filter(lambda x: x[0].find("north") >= 0, l))

def test():
    print(is_real("aaaaa-bbb-z-y-x-123[abxyz]"))
    print(is_real("a-b-c-d-e-f-g-h-987[abcde]"))
    print(is_real("not-a-real-room-404[oarel]"))
    print(is_real("totally-real-room-200[decoy]"))


if __name__ == "__main__":
    print(solve1())
    print(solve2())
