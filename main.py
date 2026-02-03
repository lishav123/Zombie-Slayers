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

zombie = Zombie(window, -50, 494, 0.359)
zombie_pos_flip = False
zombie_speed = 2
zombie.change_state("run")

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

            if event.key == pygame.K_LEFT:
                ninja.change_state("run")
                ninja_pos_flip = True
                ninja_speed = -10

        if event.type == pygame.KEYUP:
            ninja.change_state("idle")
            ninja_speed = 0

    background.parallex(0)

    if ninja.x < 0:
        ninja.x = 0

    if ninja.x > 1100:
        ninja.x = 1100
    
    zombie.change_position(zombie.x + zombie_speed, zombie.y)
    zombie.display_state(flip=zombie_pos_flip)

    ninja.change_position(ninja.x + ninja_speed, ninja.y)
    ninja.display_state(flip=ninja_pos_flip)
    pygame.display.flip()

pygame.quit()
