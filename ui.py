import pygame
from constants import *
from blocks import Piece

class UI:
    def __init__(self, game_board_rect):
        self.display_surface = pygame.display.get_surface()
        self.game_board_rect = game_board_rect

    def draw(self, piece_queue, piece_held):
        x_pos = UNIT + self.game_board_rect.x + self.game_board_rect.width + STROKE_WIDTH
        y_pos = self.game_board_rect.y

        self.piece_queue = [Piece(piece_type, (x_pos, y_pos + index * 3 * UNIT), self.display_surface, [], center=False) for index, piece_type in enumerate(piece_queue)]

        for piece in self.piece_queue:
            piece.draw()

        self.piece_queue.clear()
        

