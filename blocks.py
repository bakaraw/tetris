import pygame
from constants import *

class Block:
    def __init__(self, initial_pos) -> None:
        self.display_surface = pygame.display.get_surface()
        self.initial_pos = initial_pos
        self.rect = pygame.Rect(self.initial_pos[0], self.initial_pos[1], UNIT, UNIT)

    def draw(self):
        pygame.draw.rect(self.display_surface, (163, 11, 44), self.rect)

    def update(self):
        print(f"{self.rect.x}")
        if self.rect.y < ROWS * UNIT:
            self.rect.y += UNIT

    def move_left(self):
        if self.rect.x > self.initial_pos[0]:
            self.rect.x -= UNIT

    def move_right(self):
        if self.rect.x < self.initial_pos[0] + (COLS - 1) * UNIT:
            self.rect.x += UNIT
