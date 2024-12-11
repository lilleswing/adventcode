from functools import lru_cache
import tqdm

@lru_cache(maxsize=None)
def count_stones(stone, blinks):
    """
    If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
    """
    if blinks == 0:
        return 1
    if stone == 0:
        return count_stones(1, blinks - 1)
    if len(str(stone)) % 2 == 0:
        left = int(str(stone)[:len(str(stone)) // 2])
        right = int(str(stone)[len(str(stone)) // 2:])
        return count_stones(left, blinks - 1) + count_stones(right, blinks - 1)
    return count_stones(stone * 2024, blinks - 1)


def part1(fname):
    stones = open(fname).readlines()
    stones = [int(x) for x in stones[0].split(' ')]
    stone_counts = [count_stones(x, 25) for x in stones]
    print(sum(stone_counts))
    stone_counts = []
    for x in tqdm.tqdm(stones):
        stone_counts.append(count_stones(x, 75))
    print(sum(stone_counts))


if __name__ == "__main__":
    part1('day11.in')