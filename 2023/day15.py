from collections import defaultdict


def funny_hash(s):
    total = 0
    for c in s:
        total += ord(c)
        total *= 17
        total %= 256
    return total


def part1(fname):
    data = open(fname).read().strip()
    chunks = data.split(',')
    retval = sum([funny_hash(x) for x in chunks])
    print(retval)


def score_boxes(boxes):
    total = 0
    for idx in range(0, 256):
        p1 = 1 + idx
        for idx2, focal_length in enumerate(boxes[idx]):
            p2 = idx2 + 1
            total += p1 * p2 * focal_length[1]
    return total


def get_box_num(chunk):
    if chunk.find('=') != -1:
        label, focal_length = chunk.split('=')
        focal_length = int(focal_length)
        box_num = funny_hash(label)
        return label, box_num, focal_length
    label = chunk[:-1]
    return label, funny_hash(label), None


def update_box(boxes, box_num, label, focal_length):
    l = boxes[box_num]
    for e in l:
        if e[0] == label:
            e[1] = focal_length
            return
    l.append([label, focal_length])


def remove_lens(boxes, box_num, label):
    l = boxes[box_num]
    for e in l:
        if e[0] == label:
            l.remove(e)
            return


def part2(fname):
    data = open(fname).read().strip()
    chunks = data.split(',')
    boxes = defaultdict(list)
    for chunk in chunks:
        label, box_num, focal_length = get_box_num(chunk)
        if chunk.endswith('-'):
            remove_lens(boxes, box_num, label)
        else:
            update_box(boxes, box_num, label, focal_length)

    retval = score_boxes(boxes)
    print(retval)


if __name__ == "__main__":
    # part1('day15.in')
    part2('day15.in')
