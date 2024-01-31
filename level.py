from pygame.math import Vector2
from component import SpriteRenderer
from player_components import PlayerMovement, PlayerRespawn
from game_object import GameObject
from collider import Collider
from endzone import EndZone
from enemy_movement import EnemyMovement
from loadxml import parse_xml
import random

# Define Colors 
from color import *

HEIGHT = 480
levels = [

    parse_xml("test.xml"),

    {
    "player_position" : Vector2(30, HEIGHT / 2),
    # enemies patrolling the vertical span of the screen x seperated by 50 pixels
    "enemies" : [
        
    ],
    "coins" : [
        {
            "patrolPoints":[Vector2(430, HEIGHT / 2) , Vector2(430, HEIGHT / 2)],
        },
    ],
    "walls" : [

    ]
},

{
    "player_position" : Vector2(30, HEIGHT / 2),
    # enemies move in a square pattern, each sequntial square has a smaller "radius"
    "enemies" : [
        {
            "patrolPoints":[Vector2(100, 0) , Vector2(500, 0), Vector2(500, HEIGHT), Vector2(100, HEIGHT)],
            "speed":3
        },
        {
            "patrolPoints":[Vector2(150, 50) , Vector2(450, 50), Vector2(450, HEIGHT - 50), Vector2(150, HEIGHT - 50)],
            "speed":5
        },
        {
            "patrolPoints":[Vector2(200, 100) , Vector2(400, 100), Vector2(400, HEIGHT - 100), Vector2(200, HEIGHT - 100)],
            "speed":7
        },
        {
            "patrolPoints":[Vector2(250, 150) , Vector2(350, 150), Vector2(350, HEIGHT - 150), Vector2(250, HEIGHT - 150)],
            "speed":10
        },
        {
            "patrolPoints":[Vector2(300, 200) , Vector2(300, 200), Vector2(300, HEIGHT - 200), Vector2(300, HEIGHT - 200)],
            "speed":random.randint(1, 10)
        },
        {
            "patrolPoints":[Vector2(350, 250) , Vector2(250, 250), Vector2(250, HEIGHT - 250), Vector2(350, HEIGHT - 250)],
            "speed":random.randint(1, 10)
        },
        {
            "patrolPoints":[Vector2(400, 300) , Vector2(200, 300), Vector2(200, HEIGHT - 300), Vector2(400, HEIGHT - 300)],
            "speed":random.randint(1, 10)
        },
        
    ],

        "coins" : [
        {
            "patrolPoints":[Vector2(600, HEIGHT / 2) , Vector2(600, HEIGHT / 2)],
        },
    ],
    "walls" : [

    ]
},

{
    "player_position" : Vector2(30, HEIGHT / 2),
    # enemies patrolling the vertical span of the screen x seperated by 50 pixels
    "enemies" : [
        {
            "patrolPoints":[Vector2(100, 0) , Vector2(100, HEIGHT)],
            "speed":3
        },
        {
            "patrolPoints":[Vector2(200, 0) , Vector2(200, HEIGHT)],
            "speed":5
        },
        {
            "patrolPoints":[Vector2(300, 0) , Vector2(300, HEIGHT)],
            "speed":7
        },
        {
            "patrolPoints":[Vector2(400, 0) , Vector2(400, HEIGHT)],
            "speed":9
        },
        {
            "patrolPoints":[Vector2(500, 0) , Vector2(500, HEIGHT)],
            "speed":11
        },
        {
            "patrolPoints":[Vector2(600, 0) , Vector2(600, HEIGHT)],
            "speed":13
        },
        {
            "patrolPoints":[Vector2(700, 0) , Vector2(700, HEIGHT)],
            "speed":15
        },
        {
            "patrolPoints":[Vector2(800, 0) , Vector2(800, HEIGHT)],
            "speed":17
        },
    ],

        "coins" : [
        {
            "patrolPoints":[Vector2(750, HEIGHT / 2) , Vector2(750, HEIGHT / 2)],
        },
    ],
    "walls" : [

    ]
},
]

class LevelManager:

    def __init__(self, ui, screen) -> None:
        self.levels = levels
        self.ui = ui
        self.screenWidth = screen[0]
        self.screenHeight = screen[1]
        self.current_level = 0
        self.load_level(levels[self.current_level])
        self.won = False

    def load_level(self, level:dict):
        # Loading in the player
        player_go = GameObject("player")
        player_go.transform.scale = Vector2(25, 25)
        player_go.transform.position = level["player_position"].copy()

        player_go.add_component(SpriteRenderer(player_go, "doesnt matter", RED, 1, dark_color = DARK_RED))
        player_go.add_component(PlayerMovement(player_go, 3))
        player_go.add_component(Collider(player_go))
        player_go.add_component(PlayerRespawn(player_go, level["player_position"].copy(), self.ui.fail_counter, self.ui.coin_counter, self))

        if "end_position" in level and level["end_position"] != None:
            end_zone2 = GameObject("end zone")
            end_zone2.add_component(SpriteRenderer(end_zone2, "dosent matter", GREEN, 0))
            end_zone2.transform.position = level["end_position"].copy()
            end_zone2.transform.scale = Vector2(25, 25)

            end_zone2.add_component(EndZone(end_zone2, self.ui, player_go, self))
            end_zone2.add_component(Collider(end_zone2))

        '''
        {
            "patrolPoints":[],
            "speed":3
        },
        '''
        # Load in all enemies
        enemies = level["enemies"]
        # Loop through the list of enemiesWIDTH
        for enemy in enemies:
            # create an enemy based on the enemy key values
            enemy_go = GameObject("enemy")
            enemy_go.transform.scale = Vector2(25, 25)
            enemy_go.transform.position = enemy["patrolPoints"][0].copy()

            enemy_go.add_component(SpriteRenderer(enemy_go, "dosent matter", BLUE, 1, True, DARK_BLUE))
            points = enemy["patrolPoints"]
            enemy_go.add_component(EnemyMovement(enemy_go, enemy["speed"], points))
            enemy_go.add_component(Collider(enemy_go))

        # Load in all coins
        coins = level["coins"]
        # Loop through the list of coinsWIDTH
        for coin in coins:
            # create an coin based on the coin key values
            coin_go = GameObject("coin")
            coin_go.transform.scale = Vector2(25, 25)
            coin_go.transform.position = coin["patrolPoints"][0].copy()

            coin_go.add_component(SpriteRenderer(coin_go, "dosent matter", YELLOW, 1, True, DARK_YELLOW))
            points = coin["patrolPoints"]
            coin_go.add_component(Collider(coin_go))

        # Load in all walls
        walls = level["walls"]
        # Loop through the list of wallsWIDTH
        for wall in walls:
            # create an wall based on the wall key values
            wall_go = GameObject("wall")
            wall_go.transform.scale = Vector2(25, 25)
            wall_go.transform.position = wall["patrolPoints"][0].copy()
            rgb = wall["wallColor"]

            wall_go.add_component(SpriteRenderer(wall_go, "dosent matter", rgb, 1))
            points = wall["patrolPoints"]
            wall_go.add_component(Collider(wall_go))

        # Create the endzones
        start_zone = GameObject("start zone")
        start_zone.add_component(SpriteRenderer(start_zone, "dosent matter", GREEN, 0))
        start_zone.transform.position = Vector2(0, 0)
        start_zone.transform.scale = Vector2(50, self.screenHeight)

        end_zone = GameObject("end zone")
        end_zone.add_component(SpriteRenderer(end_zone, "dosent matter", GREEN, 0))
        end_zone.transform.position = Vector2(self.screenWidth - 50, 0)
        end_zone.transform.scale = Vector2(50, self.screenHeight)
        end_zone.add_component(EndZone(end_zone, self.ui, player_go, self))
        end_zone.add_component(Collider(end_zone))

    def next_level(self):
        if(self.current_level == len(levels) - 1):
            print("CONGRATS YOU WIN")
            self.won = True
            return
        GameObject.all_game_objects = []
        SpriteRenderer.render_layers = []
        for layer_number in range(3):
            # add a new empty list into render layers with append
            SpriteRenderer.render_layers.append([])
        self.current_level += 1
        self.ui.level_counter.increment()
        self.load_level(levels[self.current_level])