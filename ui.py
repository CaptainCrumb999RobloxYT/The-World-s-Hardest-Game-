import pygame

ui_white = (230, 240, 255)

class TextUI:
    def __init__(self, screen, location, text, font, color):
        self.screen = screen
        self.location = location
        self.text = text
        self.font = font
        self.color = color
        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = location

    def render(self):
        self.screen.blit(self.text_surface, self.text_rect)

    def update_text(self, text):
        self.text = text
        self.text_surface = self.font.render(self.text, True, self.color)
        

class LevelCounter(TextUI):
    def __init__(self, screen, number):
        super().__init__(screen, (140,30), "LEVEL: " + str(number), pygame.font.Font("arial.ttf", 64), ui_white)

    def render(self):
        return super().render()


class FailCounter(TextUI):
    def __init__(self, screen, number, width):
        super().__init__(screen, (width - 140,30), "FAILS: " + str(number), pygame.font.Font("arial.ttf", 64), ui_white)

    def render(self):
            return super().render()
class UI:
    def __init__(self, screen, dimensions) -> None:
        self.screen = screen
        self.dimensions = dimensions
        self.level_counter = LevelCounter(screen, 1)
        self.fail_counter = FailCounter(self.screen, 0, dimensions[0])

    def render(self):
        self.level_counter.render()
        self.fail_counter.render()

    def update(self):
        self.render()
    
        