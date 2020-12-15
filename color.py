# -*- coding: utf-8 -*-
"""Contains the Color class"""


class Color:
    """Color object for the insects"""

    def __init__(self, key=True):
        """key is a color in a string or a boolean"""
        self.bool = None
        self.color_str = None

        self.colors = ('white', 'black')

        if type(key) is bool:
            self.bool = key
            self.update_color()
        elif type(key) is str:
            self.color_str = key
            self.update_bool()

    def _get_color(self):
        return self.color_str

    def _set_color(self, new_color):
        self.color_str = new_color
        self.update_bool()

    color = property(_get_color, _set_color)

    def __eq__(self, other):
        """self == other : return True if the other is the same"""
        if type(other) is Color:
            return bool(self) == bool(other)
        # probably temporary
        elif type(other) is str:
            return self.color == other
        elif type(other) is bool:
            return self.bool == other

    def __bool__(self):
        """bool(self) : return True if the color is white"""
        return self.bool

    def __repr__(self):
        """print(self) : return the color string"""
        return self.color_str

    def __contains__(self, item):
        """item in self : return True if the item is a string of a valid color"""
        return item in self.colors

    def __len__(self):
        """len(self) : return the number of colors"""
        return len(self.colors)

    def direction(self):
        """return 1 if color is white and -1 if color is black"""
        return int(bool(self))*2-1

    def update_bool(self):
        """update the bool value based on the color value"""
        if self.color == self.colors[0]:
            self.bool = True
        else:
            self.bool = False

    def update_color(self):
        """update the color value based on the bool value"""
        if bool(self):
            self.color = self.colors[0]
        else:
            self.color = self.colors[1]

    def change(self):
        """change the color"""
        self.bool = not bool(self)
        self.update_color()
