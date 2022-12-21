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
    render_layers = [[]]*3
    '''
    [
        0: [start_zone, end_zone]
        1: [player, enemy]
        2: [coin]
    ]
    '''
    def __init__(self, game_object, sprite, color, layer) -> None:
        super().__init__(game_object)
        self.sprite = sprite
        self.color = color
        SpriteRenderer.render_layers[layer].append(self)
        SpriteRenderer.print_render_layers()

    def render(self):
        pygame.draw.rect(SpriteRenderer.screen,self.color, self.game_object.transform.get_rect())

    def render_all():
        for layer in SpriteRenderer.render_layers:
            for renderer in layer:
                renderer.render()

    def print_render_layers():
        print(len(SpriteRenderer.render_layers[0]))
        print(len(SpriteRenderer.render_layers[1]))
        print(len(SpriteRenderer.render_layers[2]))
        
