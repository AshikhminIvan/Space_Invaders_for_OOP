import pygame
import sys
from hero import mainhero


def start_game():
    pygame.init()
    screen = pygame.display.set_mode((500,800))
    pygame.display.set_caption("Counter Strike 3")

    flag = True
    main_hero = mainhero(screen)
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()
        main_hero.output()

start_game()

