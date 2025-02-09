import pygame
from player import Player
from asteroidField import AsteroidField
from shot import Shot
from asteroid import Asteroid
from constants import *

def main():
    pygame.init()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables, shots)
    
    dt = 0
    clock = pygame.time.Clock()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)  
    asteroidField = AsteroidField()  

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatables.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                return
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
        for drawable in drawables:
            drawable.draw(screen)
        # player.draw(screen)
        # player.update(dt)
        # print("drawing now")
        pygame.display.flip()        
        dt = clock.tick(60)/1000   
                   
    
if __name__ == "__main__":
    main()