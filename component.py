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
        return pygame.Rect(self.position.x, self.position.y, self.scale.x, self.scale.y)

class SpriteRenderer(Component):
    screen = None
    render_layers = []

    # for
    # loop 3 times
    for layer_number in range(3):
        # add a new empty list into render layers with append
        render_layers.append([])
    
    '''
    [
        0: [start_zone, end_zone]
        1: [player, enemy]
        2: [coin]
    ]
    '''
    
    def __init__(self, game_object, sprite, color, layer, draw_as_circle = False, dark_color = None) -> None:
        super().__init__(game_object)
        self.sprite = sprite
        self.color = color
        SpriteRenderer.render_layers[layer].append(self)
        self.show = True
        self.draw_circle = draw_as_circle
        self.dark_color = dark_color

    def render(self):
        if not self.show:
            return
        rect = self.game_object.transform.get_rect()
        if self.draw_circle:  
            pygame.draw.circle(SpriteRenderer.screen,self.color, rect.center, rect.width / 2)
            if self.dark_color:
                pygame.draw.circle(SpriteRenderer.screen,self.dark_color, rect.center, rect.width / 2, 3)
        else:
            pygame.draw.rect(SpriteRenderer.screen,self.color, rect)
            if self.dark_color:
                pygame.draw.rect(SpriteRenderer.screen,self.dark_color, rect, 3)


    def render_all():
        for layer in SpriteRenderer.render_layers:
            for renderer in layer:
                renderer.render()