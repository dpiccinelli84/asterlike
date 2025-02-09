import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        print("circle init")
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def collision(self, circle):
        if self.position.distance_to(circle.position) > self.radius + circle.radius:
            return False
        return True

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass