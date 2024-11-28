import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    dt = 0
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)

    player =  Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for sprite in updatable:
            sprite.update(dt)

        for asteroid in asteroids:
            collision = asteroid.detect_collision(player)
            if collision:
                print(f"Game Over!")
                return

        screen.fill((0,0,0))

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick / 1000.0

if __name__ == "__main__":
    main()