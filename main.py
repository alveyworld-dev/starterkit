#
# Pygame Starter Kit
# Copyright 2014, AlveyLabs Inc
# 
# Version 0.2.3
# 

import sys, pygame
from source import game
from source.update import update
from source.draw import draw

def main():
    """
    Main game initilization code
    """

    # Set up pygame
    pygame.init()
    game.screen = pygame.display.set_mode(game.window_size, pygame.DOUBLEBUF)
    keys = set()

    # Set up game
    game.init()

    # Perform game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN: keys.add(event.key)
            if event.type == pygame.KEYUP: keys.discard(event.key)

        update(keys)
        draw()

    return

# Ignore this, it simply calls the main() function
if __name__ == "__main__":
    main()