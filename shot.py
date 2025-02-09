from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        print("sparo inizializzato")
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        print("sparo disegnato")
        
    def update (self, dt):
        self.position += self.velocity * dt
        print("posizione sparo aggiornata")