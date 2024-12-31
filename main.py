import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    running_state = True
    pygame.init()
    clock = pygame.time.Clock()

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (drawable,updatable)
    Asteroid.containers = (drawable,updatable, asteroids)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()


    dt = 0

    while running_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_state = False
                return
        
        for update in updatable:
            update.update(dt)

        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game Over")
                return
            

        screen.fill("black")

        for drawing in drawable:
            drawing.draw(screen)

        pygame.display.flip()

        waiting_time = clock.tick(60)
        dt = waiting_time/1000


if __name__ == "__main__":
    main()