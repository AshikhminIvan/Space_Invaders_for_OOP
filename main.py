import pygame
import sys
from hero import mainhero


def start_game():
    pygame.init()
    screen = pygame.display.set_mode((200,800))
    pygame.display.set_caption("Counter Strike 3")

    flag = True
    main_hero = mainhero(screen)
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        mainhero.move_right = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                            mainhero.move_right = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_a:
                                mainhero.move_left = True
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_d:
                                    mainhero.move_left = False









            main_hero.output()
            pygame.display.flip()


start_game()

