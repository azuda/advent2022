"""
Advent of Code 2022
Day 3
Rucksack Reorganization
"""


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
value = 1
convert = {}
for a in alphabet:
  convert[a] = value
  value += 1


def p1():
  with open("3_input.txt") as f:
    lines = f.read().splitlines()

  total = 0
  seen = []
  for line in lines:
    c1 = set(list(line[0:int(len(line)/2)]))
    c2 = set(list(line[int(len(line)/2):]))

    for char in c1:
      if char in c2:
        seen.append(char)

  for char in seen:
    total += convert[char]

  print(total)


def p2():
  with open("3_input.txt") as f:
    lines = f.read().splitlines()
  
  total = 0
  counter = 0
  three = []
  for line in lines:
    three.append(line)
    counter += 1
    if counter % 3 == 0:
      for char in three[0]:
        if (char in three[1]) and (char in three[2]):
          total += convert[char]
          three = []
          break

  print(total)


p1()
p2()
