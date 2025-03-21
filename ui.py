import pygame
from constants import UNIT, PieceType, STROKE_WIDTH
from datetime import datetime
from blocks import Piece
from text import Text


class UI:
    def __init__(self, game_board_rect):
        self.display_surface = pygame.display.get_surface()
        self.game_board_rect = game_board_rect
        self.time_text = Text("Hello, Pygame!", 250, 250,
                              font_size=36, color=(255, 255, 0))

    def draw(self, piece_queue, piece_held):
        x_pos = UNIT + self.game_board_rect.x + \
            self.game_board_rect.width + STROKE_WIDTH
        y_pos = self.game_board_rect.y

        self.piece_queue = [Piece(piece_type, (x_pos, y_pos + index * 3 * UNIT), self.display_surface, [
        ], center=False) for index, piece_type in enumerate(piece_queue)]

        for piece in self.piece_queue:
            piece.draw()

        if piece_held is not None:
            x_offset = 4
            if piece_held == PieceType.I_PIECE.value:
                x_offset = 5
            self.piece_held = Piece(piece_held, (self.game_board_rect.x - x_offset *
                                    UNIT, self.game_board_rect.y), self.display_surface, [], center=False)
            self.piece_held.draw()
        self.piece_queue.clear()
        self.time_text.draw_text(self.display_surface)

    def render_timer_txt(self, start_time):
        now = datetime.now()
        elapsed_time = now - start_time

        total_seconds = int(elapsed_time.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = elapsed_time.microseconds // 10000  # First 2 digits
        formatted_time = ""
        if hours != 0:
            formatted_time += f"{hours}:"

        if minutes != 0:
            formatted_time += f"{minutes}:"

        if seconds != 0:
            formatted_time += f"{seconds}"

        formatted_time += f".{milliseconds:02d}"

        self.time_text.text = formatted_time
        self.time_text.render_text()
