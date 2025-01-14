from constants import *
from blocks import Block, Piece
import pygame
import random

class GameBoard:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.width = COLS * UNIT
        self.height = ROWS * UNIT
        self.x = (SCREEN_WIDTH - self.width) / 2
        self.y = (SCREEN_HEIGHT - self.height) / 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.accumulator = 0
        self.tick_rate = 0.5
        
        self.key_pressed = False
        self.l_r_pressed = False

        self.u_d_pressed = False
        self.u_d_accumulator = 0

        self.all_blocks = []
        self.piece_list = [Piece(piece_type.value, (self.x, self.y), self.rect, []) for piece_type in PieceType]
        self.current_piece = self.copy_piece(random.choice(self.piece_list))
        # self.current_piece = Piece(PieceType.J_PIECE.value, (self.x, self.y), self.rect, self.all_blocks)

        self.key_accumulator = 0
        self.key_tick_rate = 3

        self.key_accumulator = 0
        self.key_tick_rate = 5


    def update(self, delta_time):
        self.input()
        pygame.draw.rect(self.display_surface, BOARD_COLOR, self.rect)
        self.accumulator += delta_time
        if self.accumulator >= self.tick_rate:
            self.accumulator = self.accumulator - self.tick_rate
            self.current_piece.update()

        if self.current_piece.reached_bottom:
            new_piece = self.copy_piece(random.choice(self.piece_list))
            for block in self.current_piece.blocks:
                for other_block in new_piece.blocks:
                    # if new piece collides with the current piece then it is game over
                    if block.rect.x == other_block.rect.x and block.rect.y == other_block.rect.y:
                        print("Game Over")
                        pygame.quit()

            # if a block is out of bounds, then game over
            for block in self.all_blocks:
                if not self.rect.contains(block.rect):
                    print("Game Over")
                    pygame.quit()

            for block in self.current_piece.blocks:
                self.all_blocks.append(block)
            self.current_piece = new_piece
            print(len(self.all_blocks))

        self.current_piece.draw()

        for block in self.all_blocks:
            block.draw()


        self.draw_grid()

    def copy_piece(self, piece: Piece):
        return Piece(piece.piece_type, piece.initial_pos, piece.game_board_rect, self.all_blocks)

    def draw_grid(self):
        for row in range(ROWS + 1):
            y = row * UNIT + self.y
            pygame.draw.line(self.display_surface, GRID_COLOR, (self.x, y), (self.width + self.x, y))
        for col in range(COLS + 1):
            x = col * UNIT + self.x
            pygame.draw.line(self.display_surface, GRID_COLOR, (x, self.y), (x, self.height + self.y))

    def input(self):
        key = pygame.key.get_pressed()
        if not self.l_r_pressed:
           if key[pygame.K_RIGHT]:
                self.current_piece.move_right()
                self.l_r_pressed = True
           elif key[pygame.K_LEFT]:
                self.current_piece.move_left()
                self.l_r_pressed = True

           # if key[pygame.K_DOWN]:
           #      print("down")
           #      self.l_r_pressed = True
        else:
            if not (key[pygame.K_RIGHT] or key[pygame.K_LEFT]):
                self.l_r_pressed = False
                self.key_accumulator = 0

        # for up key
        # this is separated from the above statement because we want the piece to rotate when left or right key is held down
        # this is to prevent up key from being pressed when left or right key is held down
        if not self.u_d_pressed:
            if key[pygame.K_UP]:
                print("up")
                self.current_piece.rotate()
                self.u_d_pressed = True
        else:
            if not key[pygame.K_UP]:
                self.u_d_pressed = False

        # when left and right key is held down
        if key[pygame.K_RIGHT]:
            self.key_accumulator += 0.3
            if self.key_accumulator >= self.key_tick_rate:
                self.current_piece.move_right()
                self.key_accumulator = 4
        elif key[pygame.K_LEFT]:
            self.key_accumulator += 0.3
            if self.key_accumulator >= self.key_tick_rate:
                self.current_piece.move_left()
                self.key_accumulator = 4
        elif key [pygame.K_DOWN]:
            self.tick_rate = 0.1

        if not key[pygame.K_DOWN]:
            self.tick_rate = 0.5
