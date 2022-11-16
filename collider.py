import pygame
from component import Component
from game_object import GameObject

class Collider(Component):
    def __init__(self, game_object) -> None:
        super().__init__(game_object)

    def update(self):
        self.collision_check()

    def collision_check(self) -> GameObject:
        for game_object in GameObject.all_game_objects:
            if game_object == self.game_object: 
                continue
            if pygame.Rect.colliderect(self.game_object.transform.get_rect(), game_object.transform.get_rect()):
                for component in self.game_object.component_list: 
                    component.on_collision(game_object)
                return game_object