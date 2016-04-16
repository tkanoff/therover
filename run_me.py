# -*- coding: utf-8 -*-

import re

from plateau import Plateau
from rover import Rover


# Get test data from the file
filename = "data.txt"

rover_index = 0

plateau_initial = {}
rovers = {}

rover_position_pattern = re.compile("(\d\ ){2}\w")
directions_position_pattern = re.compile("^[A-Z]+")

with open(filename) as f:
    for line in f:
        line = line.strip()

        # Get initial Plateau coordinates
        if not plateau_initial:
            try:
                plateau_initial['x'], plateau_initial['y'] = line.split(' ')
            except:
                print('Failed to read Plateau initial coordinates')

        if rover_index not in rovers.keys():
            rovers[rover_index] = Rover()

        position = rover_position_pattern.match(line)
        directions = directions_position_pattern.match(line)

        if position:
            rovers[rover_index].set_position(position.group(0))

        if directions:
            rovers[rover_index].set_directions(directions.group(0))

        if rovers[rover_index].is_ready():
            rover_index += 1


print plateau_initial
print rovers


plateau = Plateau(plateau_initial['x'], plateau_initial['y'])
for r in rovers.values():
    r.set_plateau(plateau)
    r.split_coordinates()



