rows = 400000

def create_grid(inp):
  trap_prefixes = ['^^.', '.^^', '^..', '..^']
  mat = []
  for i in range(rows):
    mat.append(['.'] * (len(inp) + 2))
  mat[0][1:-1] = list(inp)
  for row in range(1, rows):
    for col in range(1, len(inp)+1):
      pat = "".join(mat[row-1][col-1:col+2])
      if pat in trap_prefixes:
        mat[row][col] = '^'

  for row in range(rows):
    mat[row] = mat[row][1:-1]
  return mat


def solve1():
  inp = ".^^..^...^..^^.^^^.^^^.^^^^^^.^.^^^^.^^.^^^^^^.^...^......^...^^^..^^^.....^^^^^^^^^....^^...^^^^..^"
  mat = create_grid(inp)
  for row in mat:
    print("".join(row))
  total = 0
  for row in mat:
    for col in row:
      if col == '.':
        total += 1
  return total


if __name__ == "__main__":
  print(solve1())