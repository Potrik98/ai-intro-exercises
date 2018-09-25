import sys
import numpy
from AStar import wall, astar

filename = sys.argv[1]
input_file = open(filename, "r")
board = []
ax = 0
ay = 0
bx = 0
by = 0
y = 0
for line in input_file:
    a = []
    x = 0
    for c in line:
        if c == '#':
            a.append(wall)
        elif c == 'A':
            ax = x
            ay = y
            a.append(0)
        elif c == 'B':
            bx = x
            by = y
            a.append(0)
        else:
            a.append(0)
        x += 1
    board.append(a)
    y += 1

nmap = numpy.array(board)
print(nmap)
res = astar(nmap, (ay, ax), (by, bx))
print("---\n")

for r in res:
    nmap[r[0],r[1]] = 9

print(nmap)
