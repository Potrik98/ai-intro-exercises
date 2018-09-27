import sys
import numpy
from AStar import astar, wall
from draw import draw_board
from parser import parse_board

filename = sys.argv[1] # Read filename as command line argument

(ax, ay), (bx, by), nmap = parse_board(filename)

path = astar(nmap, (ay, ax), (by, bx)) # Calculate the shortest path

nmap[ay, ax] = -1 # Set the value of point a to -1 (used for visualisation)
nmap[by, bx] = -2 # Set the value of point b to -2 (used for visualisation)

# Declare the colors of the tiles
colors = {
       1 : (255, 255, 255),
     100 : (  0,   0, 255),
      50 : (150, 150, 150),
      10 : (  0, 150,   0),
       5 : ( 51, 255, 102),
      -1 : (  0, 255,   0),
      -2 : (255,   0,   0),
    wall : ( 60,  60,  60),
}

draw_board(nmap, colors, path)
