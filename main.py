import pygame
from constants import *



def main():

    print("Starting asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    running_state = True
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    while running_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_state = False
                return
        screen.fill("black")
        pygame.display.flip()
        waiting_time = clock.tick(60)
        dt = waiting_time/1000



if __name__ == "__main__":
    main()