import pygame

# from characters import Ninja
from characters import BackgroundParallex

from sprites import Ninja
from sprites import Zombie

pygame.init()

WIDTH, HEIGHT = 1200, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Slayer - Ninja")


background = BackgroundParallex(window, 0, -790, 2)
background.load_state()

ninja = Ninja(window, 550, 500, 0.4)
ninja_pos_flip = False
ninja_speed = 0

zombie = Zombie(window, 450, 494, 0.359)
zombie_pos_flip = False
zombie_speed = 0

fps = pygame.time.Clock()

close_window = False
while not close_window:
    fps.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ninja.change_state("run")
                ninja_pos_flip = False
                ninja.change_position(ninja.x + 10, ninja.y)
                ninja_speed = 10

            if event.key == pygame.K_s:
                zombie.change_state("run")
                zombie_pos_flip = False
                zombie.change_position(zombie.x + 10, zombie.y)
                zombie_speed = 5

            if event.key == pygame.K_a:
                zombie.change_state("run")
                zombie_pos_flip = True
                zombie.change_position(zombie.x - 10, zombie.y)
                zombie_speed = -5

            if event.key == pygame.K_LEFT:
                ninja.change_state("run")
                ninja_pos_flip = True
                ninja.change_position(ninja.x - 10, ninja.y)
                ninja_speed = -10

        if event.type == pygame.KEYUP:
            ninja.change_state("idle")
            ninja_speed = 0

            zombie.change_state("idle")
            zombie_speed = 0

    background.parallex(0)
    
    zombie.change_position(zombie.x + zombie_speed, zombie.y)
    zombie.display_state(flip=zombie_pos_flip)

    ninja.change_position(ninja.x + ninja_speed, ninja.y)
    ninja.display_state(flip=ninja_pos_flip)
    pygame.display.flip()

pygame.quit()
