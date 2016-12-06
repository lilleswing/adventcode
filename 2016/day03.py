data = [[float(y) for y in x.strip().split()] for x in open('day03.in').readlines()]

def solve1():
    count = 0
    for line in data:
        line = sorted(line)
        if line[0] + line[1] > line[2]:
            count += 1
    return count

def solve2():
    my_triangles = []
    for i in xrange(0, len(data), 3):
        block = data[i:i+3]
        for j in xrange(0, 3):
            t1 = []
            for k in xrange(0, 3):
                t1.append(block[k][j])
            my_triangles.append(t1)

    count = 0
    for line in my_triangles:
        line = sorted(line)
        if line[0] + line[1] > line[2]:
            count += 1
    return count




if __name__ == "__main__":
    #print(solve1())
    print(solve2())
