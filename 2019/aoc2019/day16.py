import numpy as np
import math

# transmission = "12345678"

PATTERN = [0, 1, 0, -1]


def calc_digit(a, index):
    my_pattern = []
    for elem in PATTERN:
        part = [elem] * (index + 1)
        my_pattern.extend(part)

    num_tiles = math.ceil(len(a) / len(my_pattern)) + 1
    block = np.tile(my_pattern, num_tiles)
    block = block[1:]
    block = block[:len(a)]

    # print(len(a), len(block))
    # assert len(a) == len(block)
    # print(a * block)
    # print(np.sum(a * block))
    # raise ValueError()
    new_val = abs(np.sum(a * block)) % 10
    return new_val


def run_fft(a):
    size = len(a)
    b = np.zeros(shape=(size,))
    for index in range(size):
        b[index] = calc_digit(a, index)
    return b


def solve1_transmission(transmission):
    a = np.zeros(shape=(len(transmission),))
    for i, c in enumerate(transmission):
        a[i] = int(c)

    for i in range(100):
        a = run_fft(a)
    result = a[:8].tolist()
    result = [str(int(x)) for x in result]
    result = "".join(result)
    print(result)
    return result


def test_solve1_sample():
    transmission = "80871224585914546619083218645595"
    result = solve1_transmission(transmission)
    assert result == "24176176"


def solve1():
    transmission = "59734319985939030811765904366903137260910165905695158121249344919210773577393954674010919824826738360814888134986551286413123711859735220485817087501645023012862056770562086941211936950697030938202612254550462022980226861233574193029160694064215374466136221530381567459741646888344484734266467332251047728070024125520587386498883584434047046536404479146202115798487093358109344892308178339525320609279967726482426508894019310795012241745215724094733535028040247643657351828004785071021308564438115967543080568369816648970492598237916926533604385924158979160977915469240727071971448914826471542444436509363281495503481363933620112863817909354757361550"
    result = solve1_transmission(transmission)
    return result


def test_solve1():
    assert solve1() == "37153056"


def calc_digit_2(transmition):
    dp = []
    index = len(transmition) - 1
    running_sum = 0
    while index >= 0:
        running_sum += transmition[index]
        dp.append(running_sum)
        index -= 1
    dp = [abs(x) % 10 for x in dp]
    return dp[::-1]


def solve2():
    transmission = "59734319985939030811765904366903137260910165905695158121249344919210773577393954674010919824826738360814888134986551286413123711859735220485817087501645023012862056770562086941211936950697030938202612254550462022980226861233574193029160694064215374466136221530381567459741646888344484734266467332251047728070024125520587386498883584434047046536404479146202115798487093358109344892308178339525320609279967726482426508894019310795012241745215724094733535028040247643657351828004785071021308564438115967543080568369816648970492598237916926533604385924158979160977915469240727071971448914826471542444436509363281495503481363933620112863817909354757361550"
    # transmission = "03036732577212944063491565474664"
    transmission = transmission * 10000
    offset = int(transmission[:7])

    transmission = transmission[offset:]
    transmission = [int(x) for x in transmission]
    for i in range(100):
        transmission = calc_digit_2(transmission)
    print(transmission[:8])
    return "".join([str(x) for x in transmission[:8]])


if __name__ == "__main__":
    solve2()
