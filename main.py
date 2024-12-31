import pygame
from constants import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

def main():
    print("Starting asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    running_state = True
    while running_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_state = False
                return
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()