#
# Pygame Starter Kit
# Copyright 2014, AlveyLabs Inc
# 

import sys
import pygame
from source import game
from source.update import update
from source.draw import draw

def main():
    """
    Main game initilization code
    """

    pygame.init()
    game.screen = pygame.display.set_mode(game.window_size, pygame.DOUBLEBUF)
    keys = []

    # Set up game
    game.init()

    # Perform game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.getpressed()

        update(keys)
        draw()

    return

if __name__ == "__main__":
    main()