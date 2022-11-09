'''
Variables
    Implement Later 
        Input axis
        Vertical - W & S || Up & Down
        Horizontal - A & D || Left & Right
    
    Input keys
    Implement Later - last keys
Method
    update input

Class
    Axis
        Positive Key
        Negative Key
        Value
Assignment: [Make the axis class] and constructur
Bonus: Make the get axis method
'''
import pygame

class Axis:
    def __init__(self, positive_key, negative_key, value) -> None:
        self.positive_key = positive_key
        self.negative_key = negative_key
        self.value = value

    # Get axis returns + or - value depending on if positive or negative key is pressed
    def get_axis(self):
        return_value = 0
        if get_key(self.positive_key):
            return_value += self.value
        elif get_key(self.negative_key):
            return_value -= self.value
        return return_value


keys = None

def get_key(key):
    return keys[key]

all_axis = {
    "Horizontal": Axis(pygame.K_d, pygame.K_a, 1),
    "Vertical": Axis(pygame.K_s, pygame.K_w, 1),
}

