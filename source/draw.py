import pygame
import graphics
import game
from sprite import Sprite

def draw():
    """
    Drawing logic
    """

    # Draw background
    game.screen.fill((40, 40, 40))
    
    # Drawing a sprite called my_sprite
    # my_sprite.draw()

    graphics.draw_text("Hello", (255, 255, 255), (50, 50))

    return