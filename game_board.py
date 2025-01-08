from constants import *
from blocks import Block
import pygame

class GameBoard:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.width = COLS * UNIT
        self.height = ROWS * UNIT
        self.x = (SCREEN_WIDTH - self.width) / 2
        self.y = (SCREEN_HEIGHT - self.height) / 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.block = Block((self.x, self.y))

    def run(self):
        pygame.draw.rect(self.display_surface, BOARD_COLOR, self.rect)
        self.draw_grid()
        self.block.update()

    def draw_grid(self):
        for row in range(ROWS + 1):
            y = row * UNIT + self.y
            pygame.draw.line(self.display_surface, GRID_COLOR, (self.x, y), (self.width + self.x, y))
        for col in range(COLS + 1):
            x = col * UNIT + self.x
            pygame.draw.line(self.display_surface, GRID_COLOR, (x, self.y), (x, self.height + self.y))
