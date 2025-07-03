import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
        # Poll for events
        for event in pygame.event.get():
            # User closed window
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        # ---------------------------------------------
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        # ---------------------------------------------
        # Update graphics
        pygame.display.flip()
        dt = clock.tick(60) / SECOND_IN_MILISECONDS

    pygame.quit()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
