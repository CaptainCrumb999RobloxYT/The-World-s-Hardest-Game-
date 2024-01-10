import pygame

ui_white = (230, 240, 255)
ui_black = (0, 0, 0)
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
        self.number = number
        super().__init__(screen, (140,30), "LEVEL: " + str(self.number), pygame.font.Font("cavestory.ttf", 64), ui_black)

    def render(self):
        return super().render()
    
    def increment(self, increase = 1):
        self.number += increase
        self.update_text("LEVEL: " + str(self.number))

class FailCounter(TextUI):
    def __init__(self, screen, width):
        self.count = 0
        super().__init__(screen, (width - 140,30), "FAILS: " + str(self.count), pygame.font.Font("cavestory.ttf", 64), ui_black)

    def render(self):
        return super().render()

    def update(self):
        self.render()

    def increment(self, increase = 1):
        self.count += increase
        self.update_text("FAILS: " + str(self.count))

class CoinCounter(TextUI):
    def __init__(self, screen, coin_count):
        self.coin_count = coin_count
        super().__init__(screen, (430,30), "COIN: " + str(self.coin_count), pygame.font.Font("cavestory.ttf", 64), ui_black)

    def render(self):
        return super().render()
    
    def increment(self, increase = 1):
        self.coin_count += increase
        self.update_text("COIN: " + str(self.coin_count))

class UI:
    def __init__(self, screen, dimensions) -> None:
        self.screen = screen
        self.dimensions = dimensions
        self.level_counter = LevelCounter(screen, 1)
        self.fail_counter = FailCounter(screen, dimensions[0])
        self.coin_counter = CoinCounter(screen, 0)

    def render(self):
        self.level_counter.render()
        self.fail_counter.render()
        self.coin_counter.render()

    def update(self):
        self.render()
    
        