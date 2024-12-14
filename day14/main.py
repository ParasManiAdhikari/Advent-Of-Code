import re
import math

file_name = "day14\input.txt"

if file_name == "day14\ex.txt":
    width, height = 11, 7
else:
    width, height = 101, 103


with open(file_name, "r") as file:
    lines = list(map(str.strip, file.readlines()))

q = [0]*4
midw, midh = width // 2, height // 2

for line in lines:
    x,y,dx,dy = tuple(map(int, re.findall(r'-?\d+', line)))
    xf = (x + (dx * 100)) % width
    yf = (y + (dy * 100)) % height

    if xf < midw:
        if yf < midh:
            q[0] += 1
        if yf > midh:
            q[1] += 1
    elif xf > midw:
        if yf < midh:
            q[2] += 1
        if yf > midh:
            q[3] += 1


print(math.prod(q))