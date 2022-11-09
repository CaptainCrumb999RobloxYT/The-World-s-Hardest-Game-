from component import Component
import pygame


class EnemyMovement(Component):
    distance_to_reach_point = 5
    
    def __init__(self, game_object, speed : float, patrol_points) -> None:
        super().__init__(game_object)
        self.speed = speed
        self.patrol_points = patrol_points
        self.current_point = 0
        # self.patrol_points[current_point]

    def distance_to_current_point(self):
        return self.game_object.transform.position.distance_to(self.patrol_points[self.current_point])

    def update(self):
        if self.distance_to_current_point() < EnemyMovement.distance_to_reach_point:
            self.current_point += 1
            if self.current_point >= len(self.patrol_points):
                self.current_point = 0

        #self.game_object.transform.position = self.game_object.transform.position.move_towards(self.patrol_points[self.current_point], self.speed)
        direction = self.patrol_points[self.current_point] - self.game_object.transform.position
        direction.scale_to_length(self.speed)
        self.game_object.transform.position += direction