import pygame
import game

class Sound():
    def __init__(self, filename):
        self.sound = pygame.mixer.Sound(game.rpath + filename)

    def play(self):
        self.sound.play()

    def stop(self):
        self.sound.stop()

class Music():
    def __init__(self, filename):
        pygame.mixer.music.load(game.rpath + filename)

    def play(self):
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()
