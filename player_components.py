from component import Component, SpriteRenderer
import pygame
import input
import math
from collider import Collider
from ui import TextUI

class PlayerMovement(Component):
    def __init__(self, game_object, speed) -> None:
        super().__init__(game_object)
        self.speed = speed
        self.last_movement = pygame.Vector2()

    def update(self):
        # gathering the input in a vector2
        inputs = pygame.Vector2(input.all_axis["Horizontal"].get_axis(), input.all_axis["Vertical"].get_axis())
        # normalizing the input
        if pygame.math.Vector2.length(inputs) != 0:
            pygame.math.Vector2.normalize_ip(inputs)
        # scale vector by movemement speed
        movement = inputs * self.speed
        self.last_movement = movement
        self.game_object.transform.position.y += movement.y
        self.game_object.transform.position.x += movement.x

class PlayerRespawn(Component):
    def __init__(self, game_object, respawn_point: pygame.Vector2, fail_counter_text: TextUI, coin_counter_text: TextUI, level_manager) -> None:
        super().__init__(game_object)
        self.respawn_point = respawn_point
        self.fail_counter_text = fail_counter_text
        self.coin_counter_text = coin_counter_text
        self.level_manager = level_manager
        
    def on_collision(self, game_object):
        if game_object.name == "end zone":
            return
        if game_object.name == "coin":
            self.coin_counter_text.increment()
            game_object.get_component(SpriteRenderer).show = False
            game_object.get_component(Collider).enabled = False
            return
        if game_object.name == "wall":
            last_movement = self.game_object.get_component(PlayerMovement).last_movement
            delta_x = self.game_object.transform.position.x - game_object.transform.position.x
            if abs(delta_x) >= 25: return
            last_delta_x = (self.game_object.transform.position.x - last_movement.x) - game_object.transform.position.x
            if abs(last_delta_x) < 25: last_movement.x = 0
            delta_y = self.game_object.transform.position.y - game_object.transform.position.y
            if abs(delta_y) >= 25: return
            last_delta_y = (self.game_object.transform.position.y - last_movement.y) - game_object.transform.position.y
            if abs(last_delta_y) < 25: last_movement.y = 0
            x_movement = math.copysign(25, delta_x) - delta_x
            y_movement = math.copysign(25, delta_y) - delta_y
            if last_movement.x != 0:
                self.game_object.transform.position.x += x_movement
                print(x_movement)
            if last_movement.y != 0:
                self.game_object.transform.position.y += y_movement
            return

        self.respawn()
        self.fail_counter_text.increment()
        

    def respawn(self):
        self.game_object.transform.position = self.respawn_point.copy()