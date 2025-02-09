import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        
    def update (self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        randomAngle = random.uniform(20, 50)
        v1 = self.velocity.rotate(randomAngle)
        v2 = self.velocity.rotate(-randomAngle)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        firstNewAsteroid = Asteroid(self.position.x, self.position.y, newRadius)
        secondNewAsteroid = Asteroid(self.position.x, self.position.y, newRadius)
        firstNewAsteroid.velocity = v1 * 1.2
        secondNewAsteroid.velocity = v2 * 1.2
        
        