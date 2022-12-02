"""
Advent of Code 2022
Day 1
Calorie Counting
"""


def p1():
  with open("1_input.txt") as f:
    lines = f.read().splitlines()

  sums = [0]
  counter = 0
  for line in lines:
    if line == "":
      sums.append(0)
      counter += 1
    else:
      sums[counter] += int(line)

  print(max(sums))


def p2():
  with open("1_input.txt") as f:
    lines = f.read().splitlines()

  sums = [0]
  counter = 0
  for line in lines:
    if line == "":
      sums.append(0)
      counter += 1
    else:
      sums[counter] += int(line)

  top_three = 0
  for i in range(3):
    top_three += max(sums)
    sums.remove(max(sums))

  print(top_three)


p1()
p2()
