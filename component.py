import random
import pygame
from pygame.math import Vector2
class Component:
    def __init__(self, game_object) -> None:
        self.game_object = game_object

    def update(self):
        pass

class Transform(Component):
    def __init__(self, game_object, position = Vector2(0, 0), rotation = 0, scale = Vector2(1, 1)) -> None:
        super().__init__(game_object)
        self.position = position
        self.rotation = rotation
        self.scale = scale


class SpriteRenderer(Component):
    screen = None
    def __init__(self, game_object, sprite, color) -> None:
        super().__init__(game_object)
        self.sprite = sprite
        self.color = color

    def update(self):
        square = pygame.Rect(self.game_object.transform.position.x, self.game_object.transform.position.y, self.game_object.transform.scale.x, self.game_object.transform.scale.y)
        pygame.draw.rect(SpriteRenderer.screen,self.color, square)