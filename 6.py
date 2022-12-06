"""
Advent of Code 2022
Day 6
Tuning Trouble
"""


def p1():
  with open("6_input.txt") as f:
    raw = f.read()

  big_str = raw[4:]
  seen = raw[:4]

  result = 4
  for char in big_str:
    if len(set([*seen])) == 4:
      break
    seen += char
    seen = seen[1:]
    result += 1

  print(result)


def p2():
  with open("6_input.txt") as f:
    raw = f.read()

  big_str = raw[14:]
  seen = raw[:14]

  result = 14
  for char in big_str:
    if len(set([*seen])) == 14:
      break
    seen += char
    seen = seen[1:]
    result += 1

  print(result)


p1()
p2()
