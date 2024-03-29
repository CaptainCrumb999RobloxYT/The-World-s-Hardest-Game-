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

def create_wall_color(doc,node,r,g,b):
    r_node = doc.createElement("r")
    r_node.setAttribute("type", "abs")
    r_text = doc.createTextNode(str(r))
    r_node.appendChild(r_text)
    node.appendChild(r_node)
    g_node = doc.createElement("g")
    g_node.setAttribute("type", "abs")
    g_text = doc.createTextNode(str(g))
    g_node.appendChild(g_text)
    node.appendChild(g_node)
    b_node = doc.createElement("b")
    b_node.setAttribute("type", "abs")
    b_text = doc.createTextNode(str(b))
    b_node.appendChild(b_text)
    node.appendChild(b_node)

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

def build_level(player_pos, end_pos, enemies, coins, walls, file):
    document = xml.dom.minidom.Document()
    level = document.createElement("level")
    level.setAttribute("index", "0")
    document.appendChild(level)

    player_pos_element = document.createElement("player_position")
    level.appendChild(player_pos_element)

    create_position(document,player_pos_element,player_pos.x,player_pos.y)

    end_pos_element = document.createElement("end_position")
    level.appendChild(end_pos_element)

    create_position(document,end_pos_element,end_pos.x,end_pos.y)



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

    walls_element = document.createElement("walls")
    level.appendChild(walls_element)

    for wall in walls:
        new_wall = document.createElement("wall")
        walls_element.appendChild(new_wall)
        create_position(document, new_wall, wall.pos.x, wall.pos.y)
        create_wall_color(document, new_wall, wall.color[0], wall.color[1], wall.color[2])

    document.writexml(file,indent = "  ", addindent = "  ", newl = "\n")
    document.unlink()