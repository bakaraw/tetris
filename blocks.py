import pygame
from constants import *

class Block:
    def __init__(self, initial_pos, color) -> None:
        self.display_surface = pygame.display.get_surface()
        self.initial_pos = initial_pos
        self.rect = pygame.Rect(self.initial_pos[0], self.initial_pos[1], UNIT, UNIT)
        self.color = color
        self.collides_with_block = False

    def draw(self):
        pygame.draw.rect(self.display_surface, self.color, self.rect)

    def move_downward(self):
        self.rect.y += UNIT

    def move_left(self):
        self.rect.x -= UNIT

    def move_right(self):
        self.rect.x += UNIT

class Piece:
    def __init__(self, piece_type, initial_pos, game_board_rect, all_blocks) -> None:
        self.display_surface = pygame.display.get_surface()
        self.piece_type = piece_type
        self.initial_pos = initial_pos
        self.x = initial_pos[0]
        self.y = initial_pos[1]
        self.blocks = []
        self.game_board_rect = game_board_rect
        self.reached_bottom = False
        self.all_blocks = all_blocks
        self.rotate_position = 0
        self.generate_piece()

    def generate_piece(self):
        if self.piece_type == PieceType.T_PIECE.value:
            self.blocks.append(Block((self.x, self.y + UNIT), T_PIECE_COLOR))
            self.blocks.append(Block((self.x + UNIT, self.y + UNIT), T_PIECE_COLOR))
            self.blocks.append(Block((self.x + UNIT * 2, self.y + UNIT), T_PIECE_COLOR))
            self.blocks.append(Block((self.x + UNIT, self.y), T_PIECE_COLOR))
        elif self.piece_type == PieceType.L_PIECE.value:
            self.blocks.append(Block((self.x, self.y), L_PIECE_COLOR))
            self.blocks.append(Block((self.x, self.y + UNIT), L_PIECE_COLOR))
            self.blocks.append(Block((self.x, self.y + 2 * UNIT), L_PIECE_COLOR))
            self.blocks.append(Block((self.x + UNIT, self.y + 2 * UNIT), L_PIECE_COLOR))
        elif self.piece_type == PieceType.I_PIECE.value:
            self.blocks.append(Block((self.x, self.y), I_PIECE_COLOR))
            self.blocks.append(Block((self.x, self.y + UNIT), I_PIECE_COLOR))
            self.blocks.append(Block((self.x, self.y + (2 * UNIT)), I_PIECE_COLOR))
            self.blocks.append((Block((self.x, self.y + (3 * UNIT)), I_PIECE_COLOR)))
        elif self.piece_type == PieceType.S_PIECE.value:
            self.blocks.append(Block((self.x, self.y + UNIT), S_PIECE_COLOR))
            self.blocks.append(Block((self.x + UNIT, self.y + UNIT), S_PIECE_COLOR))
            self.blocks.append(Block((self.x + UNIT, self.y), S_PIECE_COLOR))
            self.blocks.append(Block((self.x + 2 * UNIT, self.y), S_PIECE_COLOR))
        elif self.piece_type == PieceType.Z_PIECE.value:
            self.blocks.append(Block((self.x, self.y), Z_PIECE_COLOR))
            self.blocks.append(Block((self.x + UNIT, self.y), Z_PIECE_COLOR))
            self.blocks.append(Block((self.x + UNIT, self.y + UNIT), Z_PIECE_COLOR))
            self.blocks.append(Block((self.x + 2 * UNIT, self.y + UNIT), Z_PIECE_COLOR))
        elif self.piece_type == PieceType.J_PIECE.value:
            self.blocks.append(Block((self.x, self.y + 2 * UNIT), J_PIECE_COLOR))
            self.blocks.append(Block((self.x + UNIT, self.y + 2 * UNIT), J_PIECE_COLOR))
            self.blocks.append(Block((self.x + UNIT, self.y + UNIT), J_PIECE_COLOR))
            self.blocks.append(Block((self.x + UNIT, self.y), J_PIECE_COLOR))
        elif self.piece_type == PieceType.O_PIECE.value:
            self.blocks.append(Block((self.x, self.y), O_PIECE_COLOR))
            self.blocks.append(Block((self.x + UNIT, self.y), O_PIECE_COLOR))
            self.blocks.append(Block((self.x, self.y + UNIT), O_PIECE_COLOR))
            self.blocks.append(Block((self.x + UNIT, self.y + UNIT), O_PIECE_COLOR))
            

    def draw(self):
        for block in self.blocks:
            block.draw()

    def update(self):
        if not self.check_collision(0, UNIT):
            for block in self.blocks:
                block.move_downward()
        else:
            self.reached_bottom = True


    def move_left(self):
        if not self.check_collision(-UNIT, 0):
            for block in self.blocks:
                block.move_left()

    def move_right(self):
        if not self.check_collision(UNIT, 0):
            for block in self.blocks:
                block.move_right()

    def check_collision(self, dx, dy):
        for block in self.blocks:
            new_rect = block.rect.move(dx, dy)
            if not self.game_board_rect.contains(new_rect):
                return True
            for other_block in self.all_blocks:
                if new_rect.colliderect(other_block.rect):
                    print("collided")
                    return True
        return False
    
    def rotate(self):
        self.rotate_position = (self.rotate_position + 1) % 4
        offsets = ROTATION_OFFSETS[self.piece_type][self.rotate_position]
        for block, (dx, dy) in zip(self.blocks, offsets):
            block.rect.x += dx * UNIT
            block.rect.y += dy * UNIT 


