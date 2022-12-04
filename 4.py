"""
Advent of Code 2022
Day 4
Camp Cleanup
"""


def p1():
  with open("4_input.txt") as f:
    lines = list(f)
  
  total = 0
  for line in lines:
    line = line.split(",")
    p1 = line[0].split("-")
    p1 = [int(x) for x in p1]
    p2 = line[1].strip("\n").split("-")
    p2 = [int(x) for x in p2]

    r1 = p1[1] - p1[0]
    r2 = p2[1] - p2[0]
    if p1 == p2:
      total += 1
    elif r1 < r2:
      if (p1[1] <= p2[1]) and (p1[0] >= p2[0]):
        total += 1
    elif r1 > r2:
      if (p2[1] <= p1[1]) and (p2[0] >= p1[0]):
        total += 1

  print(total)


def p2():
  with open("4_input.txt") as f:
    lines = list(f)
  
  total = 0
  for line in lines:
    line = line.split(",")
    p1 = set([int(x) for x in range(int(line[0].split("-")[0]), int(line[0].split("-")[1]) + 1)])
    p2 = set([int(x) for x in range(int(line[1].split("-")[0]), int(line[1].split("-")[1]) + 1)])
    if p1.intersection(p2):
      total += 1
    
  print(total)


p1()
p2()
