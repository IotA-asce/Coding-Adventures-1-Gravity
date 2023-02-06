"""
game runner
"""

import sys
import pygame as pg


def run_game(_width=1920, _height=1080, _fps=60):
    """
    undocumented
    """

    pg.init()

    screen = pg.display.set_mode((_width, _height))
    clock = pg.time.Clock()

    surface = pg.Surface((1, 1))
    surface.fill("White")

    screen.blit(surface, (990, 540))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()




        pg.display.update()
        clock.tick(_fps)

run_game()
