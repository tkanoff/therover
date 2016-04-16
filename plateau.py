# -*- coding: utf-8 -*-

from custom_exceptions.bad_plateau_init import BadPlateauInit


class Plateau:

    upper_x = 0
    upper_y = 0

    def __init__(self, upper_x, upper_y):
        if upper_x <= 0:
            raise BadPlateauInit

        if upper_y <= 0:
            raise BadPlateauInit

        self.upper_x = upper_x
        self.upper_y = upper_y

    def can_move(self, current_x=None, current_y=None, x_add=None, y_add=None):
        # Decide whether a rover can move where it intents to move to
        # Rover's moves are bounded by 0,0 - x,y

        if current_x:
            try:
                return 0 <= (current_x + x_add) <= self.upper_x
            except:
                print "Cannot move from current X %s to %s" % (str(current_x), str(x_add))
                return False

        if current_y:
            try:
                return 0 <= (current_y + y_add) <= self.upper_y
            except:
                print "Cannot move from current Y %s to %s" % (str(current_y), str(y_add))
                return False

    def can_deploy_to(self, x, y):
        # Decide whether a rover can be deployed to the initial
        # coordinates (x, y).
        # Returns True if both x and y are inside a square of plateau's 0,0 - x,y
        return (0 <= x <= self.upper_x) and (0 <= y <= self.upper_y)

