import pygame
from pygame.math import Vector2
import random
import time
import xml
from component import SpriteRenderer
from player_components import PlayerMovement, PlayerRespawn
from game_object import GameObject
import input
from enemy_movement import EnemyMovement
from collider import Collider
from endzone import EndZone
from ui import UI
from level import LevelManager

WIDTH = 850
HEIGHT = 500
FPS = 60

# Define Colors 
from color import *

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
pygame.mixer.music.load("carefree.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.5)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
SpriteRenderer.screen = screen
pygame.display.set_caption("The World's Hardest Game")
clock = pygame.time.Clock()     ## For syncing the FPS

background = pygame.image.load("bg.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Game Variables
# Other helper objects
ui = UI(screen, (WIDTH,HEIGHT))

level_manager = LevelManager(ui, (WIDTH, HEIGHT))




# # Gameobjects
# #region Playerdd
# player_go = GameObject("player")
# player_go.transform.scale = Vector2(25, 25)
# player_go.transform.position = Vector2(WIDTH / 2, HEIGHT / 2)

# player_go.add_component(SpriteRenderer(player_go, "doesnt matter", RED, 1))
# player_go.add_component(PlayerMovement(player_go, 3))
# player_go.add_component(Collider(player_go))
# player_go.add_component(PlayerRespawn(player_go, Vector2(10,10), ui.fail_counter))
# #endregion

# #region Enemy


# #endregion

# #region endzones


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
    # print(1 / delta_time)

    # Game Logic
    input.keys = pygame.key.get_pressed()
    
    # Draw/render
    screen.blit(background, (0,0))
    # for j in range(0,HEIGHT,50):
    #     for i in range(0,WIDTH,50):
    #         screen.blit(background, (i,j))
    GameObject.update_all_game_objects()

    SpriteRenderer.render_all()

    # render all ui elements
    ui.update()
    ## Done after drawing everything to the screen
    pygame.display.flip()

    if level_manager.won:
        running = False

pygame.quit()