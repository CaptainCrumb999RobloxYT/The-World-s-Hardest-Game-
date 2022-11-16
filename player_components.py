from component import Component
import pygame
import input

class PlayerMovement(Component):
    def __init__(self, game_object, speed) -> None:
        super().__init__(game_object)
        self.speed = speed

    def update(self): 
        self.game_object.transform.position.y += input.all_axis["Vertical"].get_axis()
        self.game_object.transform.position.x += input.all_axis["Horizontal"].get_axis()

class PlayerRespawn(Component):
    def __init__(self, game_object, respawn_point: pygame.Vector2) -> None:
        super().__init__(game_object)
        self.respawn_point = respawn_point

    def on_collision(self, game_object):
        self.respawn()

    def respawn(self):
        self.game_object.transform.position = self.respawn_point.copy()
