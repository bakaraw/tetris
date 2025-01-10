import enum
import pygame
from constants import *

class Block:
    def __init__(self, initial_pos, color) -> None:
        self.display_surface = pygame.display.get_surface()
        self.initial_pos = initial_pos
        self.rect = pygame.Rect(self.initial_pos[0], self.initial_pos[1], UNIT, UNIT)
        self.in_right_bound = False
        self.in_left_bound = False
        self.in_bottom_bound = False
        self.color = color

    def draw(self):
        pygame.draw.rect(self.display_surface, self.color, self.rect)

    def update(self):
        if self.rect.y < ROWS * UNIT:
            self.rect.y += UNIT

    def move_left(self):
        # if self.rect.x > self.initial_pos[0]:
        #     self.rect.x -= UNIT
        self.rect.x -= UNIT

    def move_right(self):
        # if self.rect.x < self.initial_pos[0] + (COLS - 1) * UNIT:
        #     self.rect.x += UNIT
        self.rect.x += UNIT

class Piece:
    def __init__(self, piece_type, initial_pos) -> None:
        self.display_surface = pygame.display.get_surface()
        self.piece_type = piece_type
        self.initial_pos = initial_pos
        self.x = initial_pos[0]
        self.y = initial_pos[1]
        self.blocks = []
        self.generate_blocks()

    def generate_blocks(self):
        if self.piece_type == PieceType.T_PIECE.value:
            self.blocks.append(Block((self.x, self.y + UNIT), T_PIECE_COLOR))
            self.blocks.append(Block((self.x + UNIT, self.y + UNIT), T_PIECE_COLOR))
            self.blocks.append(Block((self.x + UNIT * 2, self.y + UNIT), T_PIECE_COLOR))
            self.blocks.append(Block((self.x + UNIT, self.y), T_PIECE_COLOR))

    def update(self):
        for block in self.blocks:
            block.draw()

    def move_left(self):
        for block in self.blocks:
            block.move_left()

    def move_right(self):
        for block in self.blocks:
            block.move_right()
