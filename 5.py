"""
Advent of Code 2022
Day 5
Supply Stacks
"""


def parse_input():
  with open("5_input.txt", "r") as f:
    lines = list(f)
  
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
      i += 1

  for i in crates_dict.keys():
    crates_dict[i] = [x for x in crates_dict[i] if x != " "]

  orders_raw = []
  for row in range(10, len(lines)):
    orders_raw.append(lines[row].strip("\n"))
  
  orders = []
  for order in orders_raw:
    orders.append([int(i) for i in order.split() if i.isdigit()])
  
  return crates_dict, orders


def p1():
  inputs = parse_input()
  crates_dict = inputs[0]
  orders = inputs[1]
  
  for order in orders:
    amount = order[0]
    start = crates_dict[order[1]]
    dest = crates_dict[order[2]]

    chunk = start[-amount:]
    dest.extend(reversed(chunk))
    del start[-amount:]

    for i in crates_dict.keys():
      crates_dict[i] = [x for x in crates_dict[i] if x != " "]

  print("".join([crates_dict[i][-1] for i in crates_dict.keys()]))


def p2():
  inputs = parse_input()
  crates_dict = inputs[0]
  orders = inputs[1]
  
  for order in orders:
    amount = order[0]
    start = crates_dict[order[1]]
    dest = crates_dict[order[2]]

    chunk = start[-amount:]
    dest.extend(chunk)
    del start[-amount:]

    for i in crates_dict.keys():
      crates_dict[i] = [x for x in crates_dict[i] if x != " "]

  print("".join([crates_dict[i][-1] for i in crates_dict.keys()]))


p1()
p2()
