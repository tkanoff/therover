# -*- coding: utf-8 -*-


class Rover:
    position = None
    directions = None

    def __init__(self):
        pass

    def set_directions(self, directions):
        self.directions = directions

    def set_position(self, position):
        self.position = position

    def is_ready(self):
        return self.position and self.directions

    def __repr__(self):
        return '<%s object. Position: %s; Directions: %s>' \
               % (self.__class__.__name__, str(self.position), str(self.directions))
