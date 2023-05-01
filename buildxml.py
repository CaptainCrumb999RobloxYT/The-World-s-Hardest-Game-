import xml.dom.minidom

def create_position(doc,node,x,y,x_type = "abs",y_type = "abs"):
    x_node = doc.createElement("x")
    x_node.setAttribute("type", x_type)
    x_text = doc.createTextNode(str(x))
    x_node.appendChild(x_text)
    node.appendChild(x_node)
    y_node = doc.createElement("y")
    y_node.setAttribute("type", y_type)
    y_text = doc.createTextNode(str(y))
    y_node.appendChild(y_text)
    node.appendChild(y_node)

def create_patrol_point(doc, node, pos):
    patrol_point_element = doc.createElement("patrol_point")
    node.appendChild(patrol_point_element)
    create_position(doc, patrol_point_element, pos.x, pos.y)

def create_enemy(doc, node, enemy):
    enemy_element = doc.createElement("enemy")
    node.appendChild(enemy_element)
    patrol_points_element = doc.createElement("patrol_points")
    enemy_element.appendChild(patrol_points_element)
    for point in enemy.patrolpoints:
        create_patrol_point(doc, patrol_points_element, point)

def build_level(player_pos, enemies, coins, name):
    document = xml.dom.minidom.Document()
    level = document.createElement("level")
    level.setAttribute("index", "0")
    document.appendChild(level)

    player_pos_element = document.createElement("player_position")
    level.appendChild(player_pos_element)

    create_position(document,player_pos_element,player_pos.x,player_pos.y)



    enemies_element = document.createElement("enemies")
    level.appendChild(enemies_element)

    for enemy in enemies:
        create_enemy(document, enemies_element, enemy)

    coins_element = document.createElement("coins")
    level.appendChild(coins_element)

    for coin in coins:
        new_coin = document.createElement("coin")
        coins_element.appendChild(new_coin)
        create_position(document, new_coin, coin.pos.x, coin.pos.y)

    document.writexml(open(name, "w"), indent = "  ", addindent = "  ", newl = "\n")
    document.unlink()