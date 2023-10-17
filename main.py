import pygame
import sys


def start_game():
    pygame.init()
    screen = pygame.display.set_mode((500,800))
    pygame.display.set_caption("Counter Strike 3")

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()

start_game()

