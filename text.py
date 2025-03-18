import pygame


class Text:
    def __init__(self, text, x, y, font_size=30,
                 color=(255, 255, 255), font_name=None, antialias=True):
        self.font_size = font_size
        self.x = x
        self.y = y
        self.color = color
        self.font_name = font_name
        self.antialias = antialias
        self.text = text

        # Initialize Pygame font
        pygame.font.init()
        self.font = pygame.font.Font(pygame.font.match_font(
            font_name) if font_name else None, font_size)

        # Render initial text
        self.render_text()

    def render_text(self):
        self.text_surface = self.font.render(
            self.text, self.antialias, self.color)
        self.text_rect = self.text_surface.get_rect(center=(self.x, self.y))

    def update_text(self, new_text):
        self.text = new_text
        self.render_text()

    def draw_text(self, surface):
        surface.blit(self.text_surface, self.text_rect)

    def set_text(self, text):
        self.text = text
        self.render_text()
