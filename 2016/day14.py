import hashlib

inp = 'jlmsuwbz'
pat_three = r".*(\w)\1{2,}.*"
pat_five = r".*(\w)\1{4,}.*"
which_key = 64


def get_triple(s):
  elems = set()
  for i in range(3, len(s)+1):
    s1 = set(s[i - 3:i])
    if len(s1) == 1:
      elems.add(list(s1)[0])
      return list(s1)[0]
  return None


def get_fives(s):
  fives = set()
  for i in range(5, len(s)+1):
    s1 = set(s[i - 5:i])
    if len(s1) > 1:
      continue
    fives.add(list(s1)[0])
  return fives


def hash_value(s, stride=0):
  m = hashlib.md5()
  m.update(bytes(s, encoding='UTF-8'))
  s = m.hexdigest()
  for i in range(stride):
    m = hashlib.md5()
    m.update(bytes(s, encoding='UTF-8'))
    s = m.hexdigest()
  return s


def solve1(stride=0):
  triples = list()
  ver_triples = set()
  index = 0
  while len(ver_triples) < which_key:
    s = hash_value(str(inp) + "%d" % index, stride)

    fives = get_fives(s)
    for letter in fives:
      for trip_index, trip_letter in triples:
        if trip_index + 1000 >= index and trip_letter == letter:
          ver_triples.add(trip_index)

    trip = get_triple(s)
    if trip is not None:
      triples.append((index, trip))
    index += 1
  # print(sorted(ver_triples))
  # print(len(ver_triples))
  return sorted(ver_triples)[which_key - 1]


def solve2():
  return solve1(2016)


if __name__ == "__main__":
  print(solve1())
  print(solve2())

