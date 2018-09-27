import sys
import numpy
from AStar import wall, astar
from draw import draw_board

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
path = astar(nmap, (ay, ax), (by, bx))
for r in path:
    nmap[r[0],r[1]] = -1 # Set solution tiles to -1

nmap[ay, ax] = -2 # Set the value of a to -2 (used for visualisation)
nmap[by, bx] = -3 # Set the value of b to -3 (used for visualisation)

# Declare the colors of the tiles
colors = {
    0 : (255, 255, 255),
    1 : ( 60,  60,  60),
   -1 : (255, 255,   0),
   -2 : (  0, 255,   0),
   -3 : (255,   0,   0)
}

draw_board(nmap, colors)
