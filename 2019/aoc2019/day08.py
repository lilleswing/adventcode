from aoc2019 import read_file
import numpy as np


def calc_checksum(layer):
    num_ones = np.sum(layer == 1)
    num_twos = np.sum(layer == 2)
    return num_ones * num_twos


def solve1():
    l = read_file('day8.in')
    l = [int(x) for x in list(l)[0]]
    width = 25
    height = 6

    index = 0
    layers = []
    while index < len(l):
        layer = np.zeros((height, width))
        for h in range(height):
            for w in range(width):
                layer[h][w] = l[index]
                index += 1
        layers.append(layer)

    min_zeros = 1000000
    checksum = None
    for layer in layers:
        num_zeros = np.sum(layer == 0)
        if num_zeros < min_zeros:
            min_zeros = num_zeros
            checksum = calc_checksum(layer)

    return checksum


def calc_single_layer(layers):
    height = layers[0].shape[0]
    width = layers[0].shape[1]
    new_layer = np.zeros(layers[0].shape)

    for h in range(height):
        for w in range(width):
            for layer in layers:
                if layer[h][w] != 2:
                    new_layer[h][w] = layer[h][w]
                    break
    return new_layer


def test_solve1():
    assert solve1() == 2500

