from constants import *
import pygame

from player import Player


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True
    
    updatable, drawable = pygame.sprite.Group(), pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
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
