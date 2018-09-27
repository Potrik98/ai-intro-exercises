import sys
import numpy
from AStar import astar, wall
from draw import draw_board
from parser import parse_board, tiles

filename = sys.argv[1] # Read filename as command line argument

(ax, ay), (bx, by), nmap = parse_board(filename)

path = astar(nmap, (ay, ax), (by, bx)) # Calculate the shortest path

nmap[ay, ax] = -1 # Set the value of point a to -1 (used for visualisation)
nmap[by, bx] = -2 # Set the value of point b to -2 (used for visualisation)

# Declare the colors of the tiles
colors = {
    tiles['.'] : (255, 255, 255),
    tiles['w'] : (  0,   0, 255),
    tiles['m'] : (150, 150, 150),
    tiles['f'] : (  0, 150,   0),
    tiles['g'] : ( 51, 255, 102),
    tiles['r'] : (153, 109,  22),
    wall       : ( 60,  60,  60),
    -1         : (  0, 255,   0),
    -2         : (255,   0,   0),
}

draw_board(nmap, colors, path)
