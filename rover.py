# -*- coding: utf-8 -*-

import re


class Rover:
    position = None
    directions = None
    plateau = None

    position_x = None
    position_y = None
    position_facing = None

    direction_transitions = {
        'L': {
            'N': 'W',
            'W': 'S',
            'S': 'E',
            'E': 'N',
        },
        'R': {
            'N': 'E',
            'E': 'S',
            'S': 'W',
            'W': 'N',
        }
    }

    def __init__(self):
        self. map_transitions = {
            'E': {
                'steps': 1,
                'update': 'x',
            },
            'N': {
                'steps': 1,
                'update': 'y',
            },
            'S': {
                'steps': -1,
                'update': 'y',
            },
            'W': {
                'steps': -1,
                'update': 'x',
            },
        }

    def set_directions(self, directions):
        self.directions = directions

    def set_position(self, position):
        self.position = position

    def set_plateau(self, plateau):
        self.plateau = plateau

    def is_ready(self):
        return self.position and self.directions

    def deploy(self):
        if self.plateau.can_deploy_to(self.position_x, self.position_y):
            print "Getting to the position"
        else:
            print "Cannot move to the position"

    def move(self):
        for command in self.directions:
            if command in ['L', 'R']:
                self.position_facing = self.direction_transitions[command][self.position_facing]

            if command == 'M':
                # TODO: this can be made better by using self.* entities or some consts
                update_coord = self.map_transitions[self.position_facing]['update']

                if update_coord == 'x':
                        self.position_x += self.map_transitions[self.position_facing]['steps']

                if update_coord == 'y':
                        self.position_y += self.map_transitions[self.position_facing]['steps']

    def split_coordinates(self):
        split_coords_pattern = re.compile("(\d{1}) (\d{1}) ([NESW]{1})")
        coords = split_coords_pattern.match(self.position)

        self.position_x = int(coords.group(1))
        self.position_y = int(coords.group(2))
        self.position_facing = coords.group(3)

    def __repr__(self):
        return '<%s object. Position: %s; Directions: %s>' \
               % (self.__class__.__name__, str(self.position), str(self.directions))

