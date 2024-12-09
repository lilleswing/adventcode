from copy import deepcopy
from multiprocessing import pool
import tqdm


def make_layout(data):
    layout = []
    idx = 0
    file_num = 0
    is_file = True
    while idx < len(data):
        if is_file:
            file_len = int(data[idx])
            my_file = [file_num] * file_len
            file_num += 1
            layout += my_file
        else:
            free_space_len = int(data[idx])
            free_space = ['.'] * free_space_len
            layout += free_space
        idx += 1
        is_file = not is_file
    return layout


def pack_layout(layout):
    layout = deepcopy(layout)
    start, end = 0, len(layout) - 1
    while start < end:
        if layout[start] != '.':
            start += 1
            continue
        if layout[end] == '.':
            end -= 1
            continue
        layout[start], layout[end] = layout[end], layout[start]
    return layout


def part1(fname):
    data = open(fname).readlines()
    data = [x.strip() for x in data][0]
    layout = make_layout(data)
    print(layout)
    packed_layout = pack_layout(layout)

    checksum = 0
    for idx, e in enumerate(packed_layout):
        if e == '.':
            break
        checksum += idx * e
    print(packed_layout)
    print(checksum)


def make_layout2(data):
    # type, start, size
    layout = []
    idx = 0
    file_num = 0
    is_file = True
    layout_idx = 0
    while idx < len(data):
        if is_file:
            file_len = int(data[idx])
            layout.append(('f', layout_idx, file_len, file_num))
            file_num += 1
            layout_idx += file_len
        else:
            free_space_len = int(data[idx])
            layout.append(('s', layout_idx, free_space_len, 0))
            layout_idx += free_space_len
        idx += 1
        is_file = not is_file
    return layout

def move_file2(layout, to_move):
    """
    """
    layout = deepcopy(layout)
    target_block = None
    for block in layout:
        if block[0] != 's':
            continue
        if block[1] >= to_move[1]:
            continue
        if block[2] >= to_move[2]:
            target_block = block
            break
    if target_block is None:
        return layout
    # Remove old space block, to_move block from layout
    layout.remove(target_block)
    layout.remove(to_move)
    # add two new blocks -- to_move starting at target_block, and one for leftover space
    new_block = ('f', target_block[1], to_move[2], to_move[3])
    new_space = ('s', target_block[1] + to_move[2], target_block[2] - to_move[2], 0)
    layout.append(new_block)
    layout.append(new_space)
    layout = sorted(layout, key=lambda x:x[1])
    return layout


def imap_helper(args):
    return move_file2(*args)


def pack_layout2(layout):
    to_move = [x for x in layout if x[0] == 'f']
    to_move = to_move[::-1]

    for f in tqdm.tqdm(to_move):
        layout = move_file2(layout, f)
    return layout

def part2(fname):
    data = open(fname).readlines()
    data = [x.strip() for x in data][0]
    layout = make_layout2(data)
    packed_layout = pack_layout2(layout)
    checksum = 0
    for my_type,start_idx, flen, f_idx in packed_layout:
        if my_type == '.':
            continue
        for i in range(start_idx, flen+start_idx):
            checksum += i * f_idx
    print(checksum)


if __name__ == "__main__":
    # part1("day09.in")
    part2('day09.in')
