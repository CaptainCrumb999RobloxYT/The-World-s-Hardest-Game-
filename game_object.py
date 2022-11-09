import pygame
import component

class GameObject:
    
    all_game_objects = []
    def __init__(self, name) -> None:
        self.name = name
        self.transform = component.Transform(self)
        self.component_list = []
        GameObject.all_game_objects.append(self) 

    def update(self) -> None:
        for component in self.component_list:
            component.update()

    def add_component(self, component):
        self.component_list.append(component)

    def get_component(self, component_type):
        for component in self.component_list:
            if isinstance(component, component_type):
                return component
        return None


    def update_all_game_objects():
        for game_object in GameObject.all_game_objects:
            game_object.update()