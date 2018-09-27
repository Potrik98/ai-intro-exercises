import numpy
from PIL import Image, ImageDraw

TILE_SIZE = 32

def draw_board(board: numpy.ndarray,
               colors: dict):
    image = Image.new(
        'RGB',
        (board.shape[1] * TILE_SIZE, board.shape[0] * TILE_SIZE),
        color=(0,0,0))
    draw = ImageDraw.Draw(image)
    for y in range(board.shape[0]):
        for x in range(board.shape[1]):
            x0 = x * TILE_SIZE + 1
            x1 = x0 + TILE_SIZE - 2
            y0 = y * TILE_SIZE + 1
            y1 = y0 + TILE_SIZE - 2
            draw.rectangle([(x0, y0), (x1 ,y1)], fill=colors[board[y,x]])
    image.show()
