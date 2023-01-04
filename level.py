from pygame.math import Vector2
from component import SpriteRenderer
from player_components import PlayerMovement, PlayerRespawn
from game_object import GameObject
from collider import Collider

class LevelManager:
    '''
    level = {
        player_spawn_point: Vector2,
        end_zones = [rects, rects]
        enemies = {
            enemy1 = {
                patrolPoints: [Vector2]
            },
            enemy2 = {
                patrolPoints: []
            }
        }
    }
    '''

    def __init__(self, ui) -> None:
        self.levels = []
        self.ui = ui


    def load_level(self, level:dict):
        # Loading in the player
        player_go = GameObject("player")
        player_go.transform.scale = Vector2(25, 25)
        player_go.transform.position = level["player_position"]

        player_go.add_component(SpriteRenderer(player_go, "doesnt matter", (255, 0, 0), 1))
        player_go.add_component(PlayerMovement(player_go, 3))
        player_go.add_component(Collider(player_go))
        player_go.add_component(PlayerRespawn(player_go, level["player_position"], self.ui.fail_counter))

        # Load in all enemies
            # Loop through the list of enemies

            # create an enemy based on the enemy values

        # Create the endzones