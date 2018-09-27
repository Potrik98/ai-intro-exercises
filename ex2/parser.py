import numpy
from AStar import wall

# movement cost of the different tiles
tiles = {
    '.' : 1, # an empty tile has a cost of 1
    '#' : wall,
    'w' : 100,
    'm' : 50,
    'f' : 10,
    'g' : 5,
    'r' : 1
}

def parse_board(file_name: str):
    input_file = open(file_name, "r")
    board = []
    ax = 0
    ay = 0
    bx = 0
    by = 0

    y = 0
    for line in input_file:
        a = []
        x = 0
        for c in line.strip(): # Remove newline and whitespace
            if c == 'A':
                ax = x
                ay = y
                a.append(1)
            elif c == 'B':
                bx = x
                by = y
                a.append(1)
            else:
                a.append(tiles[c])
            x += 1
        board.append(a)
        y += 1
    return (ax, ay), (bx, by), numpy.array(board)
