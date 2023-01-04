import pygame
from pygame.math import Vector2
import random
import time
from component import SpriteRenderer
from player_components import PlayerMovement, PlayerRespawn
from game_object import GameObject
import input
from enemy_movement import EnemyMovement
from collider import Collider
from endzone import EndZone
from ui import UI
from level import LevelManager

WIDTH = 640
HEIGHT = 480
FPS = 60

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
SpriteRenderer.screen = screen
pygame.display.set_caption("<Your game>")
clock = pygame.time.Clock()     ## For syncing the FPS

# Game Variables
# Other helper objects
ui = UI(screen, (WIDTH,HEIGHT))

level_manager = LevelManager(ui)


example_level = {
    "player_position" : Vector2(WIDTH / 2, HEIGHT / 2),
    "enemies" : [
        {
            "patrolPoints":[],
            "speed":[]
        },
    ],
    "end_zones":None
}


level_manager.load_level(example_level)


# # Gameobjects
# #region Player
# player_go = GameObject("player")
# player_go.transform.scale = Vector2(25, 25)
# player_go.transform.position = Vector2(WIDTH / 2, HEIGHT / 2)

# player_go.add_component(SpriteRenderer(player_go, "doesnt matter", RED, 1))
# player_go.add_component(PlayerMovement(player_go, 3))
# player_go.add_component(Collider(player_go))
# player_go.add_component(PlayerRespawn(player_go, Vector2(10,10), ui.fail_counter))
# #endregion

# #region Enemy
# enemy_go = GameObject("enemy")
# enemy_go.transform.scale = Vector2(25, 25)
# enemy_go.transform.position = Vector2(0, 0)

# enemy_go.add_component(SpriteRenderer(enemy_go, "dosent matter", BLUE, 1))
# points = [Vector2(0, 0) , Vector2(WIDTH, HEIGHT), Vector2(0, HEIGHT), Vector2(WIDTH, 0)]
# points.append(Vector2(WIDTH / 2, HEIGHT / 2))
# enemy_go.add_component(EnemyMovement(enemy_go, 3, points))
# enemy_go.add_component(Collider(enemy_go))

# #endregion

# #region endzones
# start_zone = GameObject("start zone")
# start_zone.add_component(SpriteRenderer(start_zone, "dosent matter", GREEN, 0))
# start_zone.transform.position = Vector2(25, HEIGHT / 2)
# start_zone.transform.scale = Vector2(50, HEIGHT)

# end_zone = GameObject("end zone")
# end_zone.add_component(SpriteRenderer(end_zone, "dosent matter", GREEN, 0))
# end_zone.transform.position = Vector2(WIDTH - 25, HEIGHT / 2)
# end_zone.transform.scale = Vector2(50, HEIGHT)
# end_zone.add_component(EndZone(end_zone, ui, player_go))

# #endregion endzones



## Game loop
running = True
while running:

    # Process input/events
    delta_time = clock.tick(FPS) / 1000    ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
    

    # Game Logic
    input.keys = pygame.key.get_pressed()
    
    # Draw/render
    screen.fill(BLACK)
    GameObject.update_all_game_objects()

    SpriteRenderer.render_all()

    # render all ui elements
    ui.update()
    ## Done after drawing everything to the screen
    pygame.display.flip()

pygame.quit()