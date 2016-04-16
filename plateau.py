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




