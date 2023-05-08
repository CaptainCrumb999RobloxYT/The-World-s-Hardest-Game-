from component import Component, SpriteRenderer
import pygame
import input
from collider import Collider
from ui import TextUI

class PlayerMovement(Component):
    def __init__(self, game_object, speed) -> None:
        super().__init__(game_object)
        self.speed = speed

    def update(self):
        # gathering the input in a vector2
        inputs = pygame.Vector2(input.all_axis["Horizontal"].get_axis(), input.all_axis["Vertical"].get_axis())
        # normalizing the input
        if pygame.math.Vector2.length(inputs) != 0:
            pygame.math.Vector2.normalize_ip(inputs)
        # scale vector by movemement speed
        movement = inputs * self.speed
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
        self.respawn()
        self.fail_counter_text.increment()

        

    def respawn(self):
        self.game_object.transform.position = self.level_manager.levels[self.level_manager.current_level]["player_position"]