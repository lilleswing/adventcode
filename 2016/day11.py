def solve2():
  # 8 For level 2 pairs and 12 for level one pairs
  return solve1() + 24

def solve1():
  # Solve Strontium, thulium
  answer = 3 + 2 + 2 + 2
  # 8 For level 2 pairs and 12 for level one pairs
  answer += 16 + 12
  return answer


if __name__ == "__main__":
  print(solve1())
  print(solve2())
