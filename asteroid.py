from circleshape import *
from constants import*
import pygame
from logger import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
            self.position+=(self.velocity*dt)

    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        r=random.uniform(20,50)
        a1=pygame.math.Vector2.rotate(self.velocity, random.uniform(20,50))
        a2=pygame.math.Vector2.rotate(self.velocity, -random.uniform(20,50))
        rad=self.radius-ASTEROID_MIN_RADIUS
        na1=Asteroid(self.position.x,self.position.y,rad)
        na2=Asteroid(self.position,self.position,rad)
        na1.velocity=a1*(random.uniform(11,30)/10)
        na2.velocity=a2*(random.uniform(11,30)/10)