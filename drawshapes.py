import pgzrun
from random import randint
from pgzero.builtins import Rect
WIDTH = 300
HEIGHT = 300
def draw():
    screen.fill((0, 0, 0))     # black background
    # initial color values
    r = 255
    g = 0
    b = randint(120, 255)
    # starting rectangle size
    width = WIDTH
    height = HEIGHT - 200
    # starting corner
    corner1 = (0, 0)
    for i in range(15):
        # ending corner
        corner2 = (width, height)
        # create rectangle object
        rect = Rect(corner1, corner2)
        # move rectangle to the center of the screen
        rect.center = (150, 150)
        # draw rectangle outline
        screen.draw.rect(rect, (r, g, b))
        # update width and height for next rectangle
        width -= 10
        height += 10
        # adjust colors
        r -= 10
        g += 10
pgzrun.go()