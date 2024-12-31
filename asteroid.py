import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self,screen):
        pygame.draw.polygon(screen, "white", (self.x,self.y), self.radius)

