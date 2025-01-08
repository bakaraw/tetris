import pygame
from constants import *

class Block:
    def __init__(self, pos) -> None:
        self.display_surface = pygame.display.get_surface()
        self.rect = pygame.Rect(pos[0], pos[1], UNIT, UNIT)

    def update(self):
        pygame.draw.rect(self.display_surface, (163, 11, 44), self.rect)
        print()
