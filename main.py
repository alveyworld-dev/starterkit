#
# Pygame Starter Kit
# Copyright 2014, AlveyLabs Inc
# 

import sys
import update
import draw
import pygame
import game

def main():
	pygame.init()

	game.screen = pygame.display.set_mode(game.window_size)

	while True:
		for event in pygame.event.get():
		    if event.type == pygame.QUIT: sys.exit()

		update.update()
		draw.draw()

	return

if __name__ == "__main__":
	main()