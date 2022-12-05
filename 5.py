"""
Advent of Code 2022
Day 5
Supply Stacks
"""


def parse_input():
  with open("5_input.txt", "r") as f:
    lines = list(f)
  
  # parse crates into dict
  crates = []
  for i in range(8):
    crates.append(lines[i].strip("\n"))
  crates = list(zip(*crates[::-1]))
  
  crates_dict = {}
  for i in range(1, 10):
    crates_dict[i] = []
  
  i = 1
  for row in crates:
    if row[0].isalpha():
      for char in row:
        crates_dict[i].append(char)
      crates_dict[i] = [x for x in crates_dict[i] if x != " "]
      i += 1

  # parse procedure into 2D list
  orders = []
  for row in range(10, len(lines)):
    row_str = lines[row].strip("\n")
    orders.append([int(i) for i in row_str.split() if i.isdigit()])
  
  return crates_dict, orders


def p1():
  inputs = parse_input()
  crates = inputs[0]
  orders = inputs[1]
  
  for order in orders:
    amount = order[0]
    start = crates[order[1]]
    dest = crates[order[2]]

    chunk = start[-amount:]
    dest.extend(reversed(chunk))
    del start[-amount:]

    for i in crates.keys():
      crates[i] = [x for x in crates[i] if x != " "]

  print("".join([crates[i][-1] for i in crates.keys()]))


def p2():
  inputs = parse_input()
  crates = inputs[0]
  orders = inputs[1]
  
  for order in orders:
    amount = order[0]
    start = crates[order[1]]
    dest = crates[order[2]]

    chunk = start[-amount:]
    dest.extend(chunk)
    del start[-amount:]

    for i in crates.keys():
      crates[i] = [x for x in crates[i] if x != " "]

  print("".join([crates[i][-1] for i in crates.keys()]))


p1()
p2()
