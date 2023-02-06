"""
game runner
"""

import sys
import pygame as pg
from physx import *

def run_game(_width=1920, _height=1080, _fps=60):
    """
    undocumented

    note: For the bodies a body class is to be kept inside the physx lib

    """

    pg.init()

    screen = pg.display.set_mode((_width, _height))
    clock = pg.time.Clock()

    bodies = []
    surfaces = []
    positions = []

    # surface = pg.Surface((1, 1))
    # surface.fill("White")

    # surfaces.append(surface)

    # screen.blit(surface, (990, 540))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                position = Vector2(x, y)
                positions.append(position)

                surface = pg.Surface((1, 1))
                surface.fill("White")
                surfaces.append(surface)


        for i in range(len(surfaces)):
            screen.blit(surfaces[i], (positions[i].get_x(), positions[i].get_y()))


        pg.display.update()
        clock.tick(_fps)

run_game()
