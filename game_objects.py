import pygame as pg
from physx import *
from random import randint

class Body:
    def __init__(
            self, 
            mass=1, 
            surface=pg.Surface((1, 1)), 
            dimensions=Vector2(1, 1), 
            position=Vector2(0, 0), 
            velocity=Vector2(0, 0),
            force=Vector2(0, 0)
        ) -> None:
        self.mass = mass
        self.dimensions = dimensions
        self.surface = surface
        self.position = position
        self.velocity = velocity
        self.force = force

    def get_mass(self):
        return self.mass
    
    def get_surface(self):
        return self.surface

    def get_dimensions(self):
        return self.dimensions
    
    def get_dimensions_tuple(self):
        return self.dimensions.get_x(), self.dimensions.get_y()
    
    def get_position(self):
        return self.position
    
    def get_position_tuple(self):
        return self.position.get_x(), self.position.get_y()

    def get_velocity(self):
        return self.velocity

    def get_velocity_tuple(self):
        return self.velocity.get_x(), self.velocity.get_y()

    def get_force(self):
        return self.force

    def get_force_tuple(self):
        return self.force.get_x(), self.force.get_y()
    


    def set_mass(self, mass):
        self.mass = mass

    def set_surface(self, surface):
        self.surface = surface

    def set_dimensions(self, dimensions):
        self.dimensions = dimensions

    def set_position(self, position):
        self.position = position

    def set_velocity(self, velocity):
        self.velocity = velocity

    def set_force(self, force):
        self.force = force   


    def assess_velocity(self):

        rand_vel = [-100, 100]

        if self.position.get_x() < 0 or self.position.get_x() > 1920:
            self.velocity._x *= -1

        if self.position.get_y() < 0 or self.position.get_y() > 1080:
            self.velocity._y *= -1

        if pmath.__abs__( self.velocity._x ) <= 50:
            self.velocity._x = rand_vel[randint(0,1)]

        if pmath.__abs__( self.velocity._y ) <= 50:
            self.velocity._y = rand_vel[randint(0,1)]