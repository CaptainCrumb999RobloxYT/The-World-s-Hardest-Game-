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

document = xml.dom.minidom.Document()
level = document.createElement("level")
level.setAttribute("index", "0")
document.appendChild(level)

player_position = document.createElement("player_position")
level.appendChild(player_position)

create_position(document,player_position,30,0.5,y_type = "rel")

enemies = document.createElement("enemies")
level.appendChild(enemies)

coins = document.createElement("coins")
level.appendChild(coins)

coin = document.createElement("coin")
coins.appendChild(coin)

create_position(document,coin,430,0.5,y_type = "rel")

document.writexml(open("level1.xml", "w"), indent = "    ", addindent = "    ", newl = "\n")

document.unlink()