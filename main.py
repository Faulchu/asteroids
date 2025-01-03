import pygame
from constants import *
from player import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    field = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))

        for item in drawable:
            item.draw(screen)
        for item in updatable:
            item.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                print("Game over!")
                raise exit()
            else:
                for shot in shots:
                    if asteroid.collision(shot) == True:
                        shot.kill()
                        asteroid.split()
                
        pygame.display.flip()
        dt = timer.tick(60) / 1000

    
    

if __name__== "__main__":
    main()