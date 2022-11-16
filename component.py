import random
import pygame
from pygame.math import Vector2
class Component:
    def __init__(self, game_object) -> None:
        self.game_object = game_object

    def update(self):
        pass

    def on_collision(self, game_object):
        pass

class Transform(Component):
    def __init__(self, game_object, position = Vector2(0, 0), rotation = 0, scale = Vector2(1, 1)) -> None:
        super().__init__(game_object)
        self.position = position
        self.rotation = rotation
        self.scale = scale
    
    def get_rect(self):
        return pygame.Rect(self.position.x - self.scale.x / 2, self.position.y - self.scale.y / 2, self.scale.x, self.scale.y)

class SpriteRenderer(Component):
    screen = None
    def __init__(self, game_object, sprite, color) -> None:
        super().__init__(game_object)
        self.sprite = sprite
        self.color = color

    def update(self):
        pygame.draw.rect(SpriteRenderer.screen,self.color, self.game_object.transform.get_rect())