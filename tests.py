import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the fonts
font = pygame.font.Font(None, 36)

# Initialize counters
counter1 = 0
counter2 = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                counter1 += 1
            elif event.key == pygame.K_b and counter2 > 0:
                counter2 -= 1

    # Draw everything
    screen.fill(BLACK)
    text1 = font.render(f"Counter 1: {counter1}", True, WHITE)
    text2 = font.render(f"Counter 2: {'Updated' if counter2 == 0 else counter2}", True, WHITE)

    screen.blit(text1, (10, 100))
    screen.blit(text2, (10, 150))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
