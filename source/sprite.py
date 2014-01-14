import pygame
import game

class Sprite():
    def __init__(self, texture):
        self.image = pygame.image.load(texture)
        self.rect = self.image.get_rect()
        return

    def draw(self):
        game.screen.blit(self.image, self.rect)