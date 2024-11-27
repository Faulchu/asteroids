import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.position = x, y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
                

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            neg_vector = self.velocity.rotate(-rand_angle)
            pos_vector = self.velocity.rotate(rand_angle)
            self.radius = self.radius - ASTEROID_MIN_RADIUS

            split_1 = Asteroid(self.position[0], self.position[1], self.radius)
            split_2 = Asteroid(self.position[0], self.position[1], self.radius)

            split_1.velocity = neg_vector * 1.2
            split_2.velocity = pos_vector * 1.2
