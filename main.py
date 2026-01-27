import pygame

from characters import Ninja

pygame.init()

WIDTH, HEIGHT = 1200, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Slayer - Ninja")
ninja = Ninja(window, 0, 0)

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
                print("Right Execured")

        if event.type == pygame.KEYUP:
            ninja.update_state("idle")

    window.fill((25, 25, 25))
    ninja.display_state()
    pygame.display.flip()

pygame.quit()
