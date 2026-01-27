import pygame

pygame.init()

WIDTH, HEIGHT = 1200, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Slayer - Ninja")

close_window = False
while not close_window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window = True

    window.fill((25, 25, 25))
    pygame.display.flip()

pygame.quit()
