"""
Advent of Code 2022
Day 2
Rock Paper Scissors
"""


def p1():
  with open("2_input.txt") as f:
    lines = f.read().splitlines()

  score = 0
  for line in lines:
    choose = line.split(" ")
    if choose[1] == "X":
      score += 1
      if choose[0] == "A":
        score += 3
      elif choose[0] == "C":
        score += 6
    elif choose[1] == "Y":
      score += 2
      if choose[0] == "A":
        score += 6
      elif choose[0] == "B":
        score += 3
    elif choose[1] == "Z":
      score += 3
      if choose[0] == "B":
        score += 6
      elif choose[0] == "C":
        score += 3

  print(score)


def p2():
  with open("2_input.txt") as f:
    lines = f.read().splitlines()

  score = 0
  for line in lines:
    choose = line.split(" ")
    if choose[1] == "X":
      if choose[0] == "A":
        score += 3
      elif choose[0] == "B":
        score += 1
      elif choose[0] == "C":
        score += 2
    elif choose[1] == "Y":
      if choose[0] == "A":
        score += 4
      elif choose[0] == "B":
        score += 5
      elif choose[0] == "C":
        score += 6
    elif choose[1] == "Z":
      if choose[0] == "A":
        score += 8
      elif choose[0] == "B":
        score += 9
      elif choose[0] == "C":
        score += 7

  print(score)


p1()
p2()
