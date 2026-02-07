import pygame

# from characters import Ninja
from characters import BackgroundParallex

from sprites import Ninja
from sprites import Zombie
from sprites import Kunai

pygame.init()

chance = 10

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

kunai_speed = 40
kunaies = []

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
                ninja_speed = 10
                
            if event.key == pygame.K_LEFT:
                ninja.change_state("run")
                ninja_pos_flip = True
                ninja_speed = -10

            if event.key == pygame.K_a:
                ninja.change_state("attack", endloop=True)
                
            if event.key == pygame.K_SPACE and chance != 0:
                ninja.change_state("throw", endloop=True)
                kunaies.append({"state_object": Kunai(window, ninja.x, ninja.y + 75, 0.5), "speed": -kunai_speed if ninja_pos_flip else kunai_speed})
                chance -= 1

        if event.type == pygame.KEYUP:
            ninja.change_state("idle")
            ninja_speed = 0 

    background.parallex(0)

    if ninja.x < 0:
        ninja.x = 0

    if ninja.x > 1100:
        ninja.x = 1100
    
    for index, kunai in enumerate(kunaies):
        kunai["state_object"].change_position(kunai["state_object"].x + kunai["speed"], kunai["state_object"].y) 
        kunai["state_object"].display_state(flip=kunai["speed"] < 0)

        if kunai["state_object"].x < -100 or kunai["state_object"].x > WIDTH + 100:
            del kunaies[index]


    if zombie.sprites_collide(ninja, r=100):
        zombie_speed = 0
        ninja_speed = 0
        zombie.change_state("attack")
    else:
        zombie_speed = 2
        zombie.change_state("run")

    zombie.change_position(zombie.x + zombie_speed, zombie.y)
    zombie.display_state(flip=zombie_pos_flip)

    ninja.change_position(ninja.x + ninja_speed, ninja.y)
    ninja.display_state(flip=ninja_pos_flip)
    pygame.display.flip()

pygame.quit()
