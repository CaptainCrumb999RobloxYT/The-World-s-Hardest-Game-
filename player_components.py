from component import Component
import pygame
import input
from ui import TextUI

class PlayerMovement(Component):
    def __init__(self, game_object, speed) -> None:
        super().__init__(game_object)
        self.speed = speed

    def update(self): 
        inputs = pygame.Vector2(input.all_axis["Horizontal"].get_axis(), input.all_axis["Vertical"].get_axis())
        if pygame.math.Vector2.length(inputs) != 0:
            pygame.math.Vector2.normalize_ip(inputs)
        self.game_object.transform.position.y += inputs.y
        self.game_object.transform.position.x += inputs.x

class PlayerRespawn(Component):
    def __init__(self, game_object, respawn_point: pygame.Vector2, fail_counter_text: TextUI) -> None:
        super().__init__(game_object)
        self.respawn_point = respawn_point
        self.fail_counter_text = fail_counter_text
        
    def on_collision(self, game_object):
        self.respawn()
        self.fail_counter_text.increment()

    def respawn(self):
        self.game_object.transform.position = self.respawn_point.copy()
