# -*- coding: utf-8 -*-


class BadPlateauInit(Exception):

    def __init__(self):
        Exception.__init__(
            self,
            "Wrong initial Plateau parameters"
        )
