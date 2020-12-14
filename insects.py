# -*- coding: utf-8 -*-
"""Contain the Insects classes"""


class Insect:
    """Mother of all the insects classes, should not be used on the board"""

    # one use methods
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

    def _get_position(self):
        return self.position

    def _set_position(self, new_pos):
        self.position = new_pos

    pos = property(_get_position, _set_position)

    def __repr__(self):
        return self.real_id(name=True)

    def real_id(self, name=False):
        """return non-static information about the class"""
        if self.color == 'black':
            return self.id(name).upper()
        else:
            return self.id(name)

    @staticmethod
    def id(name=False):
        """return static information about the class"""
        if name:
            return 'insect'
        return 'z'


class Bug(Insect):
    """Bug insect"""

    # one use methods
    def __init__(self, pos, color):
        Insect.__init__(self, pos, color)

    @staticmethod
    def id(name=False):
        """return information about the class"""
        if name:
            return 'bug'
        return 'g'


class Locust(Insect):
    """Locust insect"""

    # one use methods
    def __init__(self, pos, color):
        Insect.__init__(self, pos, color)

    @staticmethod
    def id(name=False):
        """return information about the class"""
        if name:
            return 'locust'
        return 'l'


class Spider(Insect):
    """Spider insect"""

    # one use methods
    def __init__(self, pos, color):
        Insect.__init__(self, pos, color)

    @staticmethod
    def id(name=False):
        """return information about the class"""
        if name:
            return 'spider'
        return 's'


class Beetle(Insect):
    """Ant insect"""

    # one use methods
    def __init__(self, pos, color):
        Insect.__init__(self, pos, color)

    @staticmethod
    def id(name=False):
        """return information about the class"""
        if name:
            return 'beetle'
        return 't'


class Bee(Insect):
    """Bee insect"""

    # one use methods
    def __init__(self, pos, color):
        Insect.__init__(self, pos, color)

    @staticmethod
    def id(name=False):
        """return information about the class"""
        if name:
            return 'bee'
        return 'b'


class Ant(Insect):
    """Ant insect"""

    # one use methods
    def __init__(self, pos, color):
        Insect.__init__(self, pos, color)

    @staticmethod
    def id(name=False):
        """return information about the class"""
        if name:
            return 'ant'
        return 'a'


insect_list = Bug, Locust, Spider, Beetle, Bee, Ant
