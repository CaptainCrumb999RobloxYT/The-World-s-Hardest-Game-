from component import Component 

class EndZone(Component):
    def __init__(self, game_object, ui, player, level_manager) -> None:
        super().__init__(game_object)
        self.ui = ui
        self.player = player
        self.level_manager = level_manager

    def on_collision(self, other):
        # if the other is the player, go to the next level
        print(other.name)
        if other.name == "player":
            self.level_manager.next_level()