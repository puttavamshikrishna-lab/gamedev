import pgzrun
from random import randint 
from pgzero.builtins import Rect


WIDTH=300
HEIGHT=300

def draw():
    screen.fill((0,0,0))

    r=255
    g=0
    b=randint(120,255)


    width=WIDTH
    height=HEIGHT-200

    corner1=(0,0)

    for i in range(15):
        corner2=(width,height)

        rect=Rect(corner1,corner2)
        rect.center=(150,150)