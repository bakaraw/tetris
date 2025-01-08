import pygame
from constants import *
from game_board import GameBoard

# hello
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True
        self.game_board = GameBoard()
        self.clock = pygame.time.Clock()

    def run(self):
        self.start_time = pygame.time.get_ticks()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()

            pygame.display.update()
            self.screen.fill(BG_COLOR)
            self.game_board.run()
            self.clock.tick(FPS)


        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
