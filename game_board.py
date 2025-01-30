from constants import *
from blocks import Block, Piece
from ui import UI
import pygame
import random

class GameBoard:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.width = COLS * UNIT
        self.height = ROWS * UNIT
        self.x = (SCREEN_WIDTH - self.width) / 2
        self.y = (SCREEN_HEIGHT - self.height) / 2
        print(self.y)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.accumulator = 0
        self.tick_rate = 0.5
        
        self.key_pressed = False
        self.l_r_pressed = False

        self.u_d_pressed = False
        self.u_d_accumulator = 0
        
        self.space_pressed = False
        self.lshift_pressed = False

        self.all_blocks = []
        new_game_board_rect = pygame.Rect(self.x, self.y - 3 * UNIT, self.width, self.height + 3 * UNIT)
        self.piece_list = [Piece(piece_type.value, (self.x, self.y - 3 * UNIT), new_game_board_rect, []) for piece_type in PieceType]
        self.piece_queue = self.generate_piece_queue()
        self.current_piece = self.piece_queue.pop(0)
        self.shadow_piece = self.copy_piece(self.current_piece)
        self.held_piece = None

        self.update_shadow_piece()
        self.ui = UI(self.rect)

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
            if self.is_game_over(new_piece):
                pygame.quit()

            for block in self.current_piece.blocks:
                self.all_blocks.append(block)
            self.current_piece = self.piece_queue.pop(0)
            self.add_piece_queue()
            self.shadow_piece = self.copy_piece(self.current_piece)
            self.check_lines()

        self.draw_grid()
        self.update_shadow_piece()
        self.draw_shadow_piece()
        self.ui.draw([piece.piece_type for piece in self.piece_queue], None)
        self.current_piece.draw()

        for block in self.all_blocks:
            block.draw()

    def drop_piece(self):
        while not self.current_piece.reached_bottom:
            self.current_piece.update()

    def draw_shadow_piece(self):
        while not self.shadow_piece.reached_bottom:
            self.shadow_piece.update()
        self.shadow_piece.draw()

    def update_shadow_piece(self):
        self.shadow_piece.x = self.current_piece.x
        self.shadow_piece.y = self.current_piece.y
        self.shadow_piece.blocks = [Block((block.rect.x, block.rect.y), SHADOW_COLOR) for block in self.current_piece.blocks]
        self.shadow_piece.all_blocks = self.all_blocks
        self.shadow_piece.reached_bottom = False
        

    def is_game_over(self, new_piece):
        for block in self.current_piece.blocks:
            for other_block in new_piece.blocks:
                # if new piece collides with the current piece then it is game over
                if block.rect.x == other_block.rect.x and block.rect.y == other_block.rect.y:
                    return True

        # if a block is out of bounds, then game over
        for block in self.all_blocks:
            if not self.rect.contains(block.rect):
                return True
        return False
    
    def check_lines(self):
        block_dic = {}
        completed_line_pos = []

        for row in range(ROWS):
            block_dic[row * UNIT + self.y] = []

        for block in self.all_blocks:
            block_dic[block.rect.y].append(True)

        for key in block_dic.keys():
            if len(block_dic[key]) == 10:
                completed_line_pos.append(key)

        # remove blocks at completed line positions
        self.all_blocks = [block for block in self.all_blocks if block.rect.y not in completed_line_pos]

        # move remaining blocks downward
        for block in self.all_blocks:
            lines_below = sum(1 for line_pos in completed_line_pos if block.rect.y < line_pos)
            if lines_below > 0:
                block.move_downward(lines_below)

        self.current_piece.all_blocks = self.all_blocks

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
                self.update_shadow_piece()
           elif key[pygame.K_LEFT]:
                self.current_piece.move_left()
                self.l_r_pressed = True
                self.update_shadow_piece()
        else:
            if not (key[pygame.K_RIGHT] or key[pygame.K_LEFT] or key[pygame.K_SPACE]):
                self.l_r_pressed = False
                self.key_accumulator = 0

        # for up key
        # this is separated from the above statement because we want the piece to rotate when left or right key is held down
        # this is to prevent up key from being pressed when left or right key is held down
        if not self.u_d_pressed:
            if key[pygame.K_UP]:
                self.current_piece.rotate()
                self.u_d_pressed = True
                self.update_shadow_piece()
        else:
            if not key[pygame.K_UP]:
                self.u_d_pressed = False

        # when space is pressed
        if not self.space_pressed:
            if key[pygame.K_SPACE]:
                self.drop_piece()
                self.space_pressed = True
        else:
            if not key[pygame.K_SPACE]:
                self.space_pressed = False

        # when shift is pressed 
        if not self.lshift_pressed:
            if key[pygame.K_LSHIFT]:
                self.hold_piece()
                self.lshift_pressed = True
        else:
            if not key[pygame.K_LSHIFT]:
                self.lshift_pressed = False


        # when left and right key is held down
        if key[pygame.K_RIGHT]:
            self.key_accumulator += 0.3
            if self.key_accumulator >= self.key_tick_rate:
                self.current_piece.move_right()
                self.key_accumulator = 4
                self.update_shadow_piece()
        elif key[pygame.K_LEFT]:
            self.key_accumulator += 0.3
            if self.key_accumulator >= self.key_tick_rate:
                self.current_piece.move_left()
                self.key_accumulator = 4
                self.update_shadow_piece()
        elif key [pygame.K_DOWN]:
            self.tick_rate = 0.1

        if not key[pygame.K_DOWN]:
            self.tick_rate = 0.5

    def generate_piece_queue(self):
        piece_queue = []
        while len(piece_queue) < 6:
            new_piece = self.copy_piece(random.choice(self.piece_list))
            if sum(1 for piece in piece_queue if piece.piece_type == new_piece.piece_type) < 2:
                piece_queue.append(new_piece)
        return piece_queue
    
    def add_piece_queue(self):
        while True:
            new_piece = self.copy_piece(random.choice(self.piece_list))
            if sum(1 for piece in self.piece_queue if piece.piece_type == new_piece.piece_type) < 2:
                self.piece_queue.append(new_piece)
                break

    def hold_piece(self):
        if self.held_piece == None:
            self.held_piece = self.copy_piece(self.current_piece)
            self.current_piece = self.piece_queue.pop(0)
            self.add_piece_queue()
        else:
            temp = self.copy_piece(self.current_piece)
            self.current_piece = self.copy_piece(self.held_piece)
            self.held_piece = temp
            print(self.held_piece.piece_type)

