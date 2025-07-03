from constants import *
import pygame


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    while running:
        # Poll for events
        for event in pygame.event.get():
            # User closed window
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("black")
        # ---------------------------------------------
        

        # ---------------------------------------------
        # Update graphics
        pygame.display.flip()
        clock.tick(60)


    pygame.quit()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
