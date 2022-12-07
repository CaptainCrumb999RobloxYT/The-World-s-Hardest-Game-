from component import Component 

class EndZone(Component):
    def __init__(self, game_object, ui, player) -> None:
        super().__init__(game_object)
        self.ui = ui
        self.player = player