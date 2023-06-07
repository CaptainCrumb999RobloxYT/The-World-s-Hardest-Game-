import xml.dom.minidom as md
import pygame

def extract_pos(node):
    x = node.getElementsByTagName("x")[0].childNodes[0].data
    x = float(x)
    y = node.getElementsByTagName("y")[0].childNodes[0].data
    y = float(y)
    return pygame.Vector2(x, y)

def parse_xml(name):
    document = md.parse(name)
    level = {}
    root = document.documentElement
    player_pos = root.getElementsByTagName("player_position")[0]
    player_pos = extract_pos(player_pos)
    enemy_nodes = root.getElementsByTagName("enemy")
    enemies = []
    for enemy in enemy_nodes:
        patrol_point_nodes = enemy.getElementsByTagName("patrol_point")
        patrol_points = []
        for patrol_point in patrol_point_nodes:
            patrol_points.append(extract_pos(patrol_point))
        enemies.append({
            "patrolPoints":patrol_points,
            "speed":5
        })
    coin_nodes = root.getElementsByTagName("coin")
    coins = []
    for coin in coin_nodes:
        coin_patrol_points = [extract_pos(coin)]
        coins.append({
            "patrolPoints":coin_patrol_points
        })
    wall_nodes = root.getElementsByTagName("wall")
    walls = []
    for wall in wall_nodes:
        wall_patrol_points = [extract_pos(wall)]
        walls.append({
            "patrolPoints":wall_patrol_points
        })
    level["player_position"] = player_pos
    level["enemies"] = enemies
    level["coins"] = coins
    level["walls"] = walls
    return level