dirs =  [
        (-1,0),
        (0,1),
        (1,0),
        (0,-1)
]
path = """R4, R3, L3, L2, L1, R1, L1, R2, R3, L5, L5, R4, L4, R2, R4, L3, R3, L3, R3, R4, R2, L1, R2, L3, L2, L1, R3, R5, L1, L4, R2, L4, R3, R1, R2, L5, R2, L189, R5, L5, R52, R3, L1, R4, R5, R1, R4, L1, L3, R2, L2, L3, R4, R3, L2, L5, R4, R5, L2, R2, L1, L3, R3, L4, R4, R5, L1, L1, R3, L5, L2, R76, R2, R2, L1, L3, R189, L3, L4, L1, L3, R5, R4, L1, R1, L1, L1, R2, L4, R2, L5, L5, L5, R2, L4, L5, R4, R4, R5, L5, R3, L1, L3, L1, L1, L3, L4, R5, L3, R5, R3, R3, L5, L5, R3, R4, L3, R3, R1, R3, R2, R2, L1, R1, L3, L3, L3, L1, R2, L1, R4, R4, L1, L1, R3, R3, R4, R1, L5, L2, R2, R3, R2, L3, R4, L5, R1, R4, R5, R4, L4, R1, L3, R1, R3, L2, L3, R1, L2, R3, L3, L1, L3, R4, L4, L5, R3, R5, R4, R1, L2, R3, R5, L5, L4, L1, L1"""
steps = path.split(r", ")


def solve1():
    def walk_block(loc, d, my_len):
        return (loc[0] + my_len * d[0], loc[1] + my_len * d[1])
    my_dir = 0
    my_loc = (0,0)
    for step in steps:
        turn = step[0]
        my_len = int(step[1:])
        if turn == 'R':
            my_dir = (my_dir + len(dirs) + 1) % len(dirs)
        else:
            my_dir = (my_dir + len(dirs) - 1) % len(dirs)
        my_loc = walk_block(my_loc, dirs[my_dir], my_len)

    print(my_loc)
    print(sum(my_loc))

def solve2():
    my_dir = 0
    my_loc = (0,0)
    visited = set()
    visited.add((0,0))
    def walk_block(loc, d, my_len):
        for i in range(my_len):
            loc = (loc[0] + d[0], loc[1] + d[1])
            if loc in visited:
                return loc, True
            visited.add(loc)
        return loc, False


    for step in steps:
        turn = step[0]
        my_len = int(step[1:])
        if turn == 'R':
            my_dir = (my_dir + len(dirs) + 1) % len(dirs)
        else:
            my_dir = (my_dir + len(dirs) - 1) % len(dirs)
        my_loc, result = walk_block(my_loc, dirs[my_dir], my_len)
        if result:
            print(my_loc)
            print(sum(my_loc))
            return
    print("No Solution")
    print(visited)

if __name__ == "__main__":
    solve2()

