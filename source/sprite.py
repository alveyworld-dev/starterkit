import pygame
import graphics

class Sprite:
    def __init__(self, pos, sz, clr):
        self.position = pos
        self.size = sz
        self.color = clr

        return

    def draw(self):
        graphics.draw_rect(self.size, self.color, self.position)
        return

    def load(self, *filename):
        return