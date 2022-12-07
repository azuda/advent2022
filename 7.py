"""
Advent of Code 2022
Day 7
No Space Left On Device
"""


from pathlib import Path


def parseData():
  with open("7_input.txt", "r") as f:
    lines = list(f)

  dirs = {}
  files = {}

  current = Path()
  dirs[Path("/")] = 0
  for line in lines:
    line = line[:-1].split(" ")
    if line[0] == "$":
      if line[1] == "cd":
        if line[2] == "..":
          current = current.parent
        else:
          current = current / line[2]
    elif line[0] == "dir":
      dirs[current / line[1]] = 0
    else:
      size = int(line[0])
      name = line[1]
      files[current / name] = size
  
  return dirs, files


def p1():
  dirs, files = parseData()

  for d in dirs:
    for s in files:
      if d in s.parents:
        dirs[d] += files[s]
  
  result = 0
  for v in dirs.values():
    if v <= 100000:
      result += v

  print(result)


def p2():
  dirs, files = parseData()

  for d in dirs:
    for s in files:
      if d in s.parents:
        dirs[d] += files[s]
  
  total_space = 70000000
  unused_space = total_space - dirs[Path("/")]

  candidates = {}
  for d in dirs:
    if dirs[d] + unused_space >= 30000000:
      candidates[d] = dirs[d]
  
  print(min(candidates.values()))


p1()
p2()
