"""
game runner
"""

import sys
from random import randint
import pygame as pg
from physx import *
from game_objects import *

def run_game(_width=1920, _height=1080, _fps=60):
    """
    undocumented

    note: For the bodies a body class is to be kept inside the physx lib

    """

    pg.init()

    screen = pg.display.set_mode((_width, _height))
    clock = pg.time.Clock()

    bodies = []

    click = 0

    while True:
        # click += 1

        # if click > 60:
            # click = 0

            # calculate the overall gravity
            # we need to test the velocity
            # calculate new position


        for body in bodies:
            for _body in bodies:
                body.velocity = _body.position - body.position

            body.velocity._x /= 10
            body.velocity._y /= 10

        for body in bodies:
            n_position = compute_new_position(body.get_position(), body.get_velocity())
            body.set_position(n_position)

        for body in bodies:
            body.assess_velocity()


        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                position = Vector2(x, y)

                surface = pg.Surface((1, 1))
                surface.fill("White")

                # body = Body(mass=4, position=position, velocity=Vector2(randint(-10, 10), randint(-20, 20)), surface=surface)
                body = Body(mass=4, position=position, velocity=Vector2(0, 0), surface=surface)
                bodies.append(body)
        
        screen.fill("Black")

        for body in bodies:
            screen.blit(body.get_surface(), body.get_position_tuple())


        pg.display.update()
        clock.tick(_fps)

run_game()
