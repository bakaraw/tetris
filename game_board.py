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
        self.accumulator = 0
        self.tick_rate = 1
        self.key_pressed = False

    def update(self, delta_time):
        self.input()
        pygame.draw.rect(self.display_surface, BOARD_COLOR, self.rect)
        self.accumulator += delta_time
        if self.accumulator >= self.tick_rate:
            self.accumulator = self.accumulator - self.tick_rate
            self.block.update()
            print("update")

        self.block.draw()
        self.draw_grid()

    def draw_grid(self):
        for row in range(ROWS + 1):
            y = row * UNIT + self.y
            pygame.draw.line(self.display_surface, GRID_COLOR, (self.x, y), (self.width + self.x, y))
        for col in range(COLS + 1):
            x = col * UNIT + self.x
            pygame.draw.line(self.display_surface, GRID_COLOR, (x, self.y), (x, self.height + self.y))

    def input(self):
        key = pygame.key.get_pressed()
        if not self.key_pressed:
           if key[pygame.K_RIGHT]:
                self.block.move_right()
                self.key_pressed = True
           elif key[pygame.K_LEFT]:
                self.block.move_left()
                self.key_pressed = True
           elif key[pygame.K_UP]:
                print("up")
                self.key_pressed = True
           elif key[pygame.K_DOWN]:
                print("down")
                self.key_pressed = True

        else:
            if not (key[pygame.K_RIGHT] or key[pygame.K_LEFT] or key[pygame.K_DOWN] or key[pygame.K_UP]):
                self.key_pressed = False