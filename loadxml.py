import xml.dom.minidom as md

def parse_xml(name):
    document = md.parse(name)
    level = {}
    root = document.documentElement
    player_pos = root.getElementsById("player_position")