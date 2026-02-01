import pygame

# from characters import Ninja
from characters import BackgroundParallex

from sprites import Ninja

pygame.init()

WIDTH, HEIGHT = 1200, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Slayer - Ninja")


background = BackgroundParallex(window, 0, -800, 2)
background.load_state()
bg_vel = 0

ninja = Ninja(window, 550, 437, 0.5)
ninja_pos_flip = False

fps = pygame.time.Clock()

close_window = False
while not close_window:
    fps.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ninja.update_state("run")
                bg_vel = -15
                ninja_pos_flip = False

            if event.key == pygame.K_LEFT:
                ninja.update_state("run")
                bg_vel = 15
                ninja_pos_flip = True

            if event.key == pygame.K_SPACE:
                ninja.update_state("throw")

        if event.type == pygame.KEYUP:
            ninja.update_state("idle")
            bg_vel = 0

    background.parallex(bg_vel)
    ninja.display_state(flip=ninja_pos_flip)
    pygame.display.flip()

pygame.quit()
