# -*- coding: utf-8 -*-
"""Contain the Board class"""


class Board:
    """Board class"""

    # one use methods
    def __init__(self, n=10):
        """constructor"""
        # initialisation of the variables with no value
        self.array = {}
        self.cells = []

        # initialisation of the values
        self.size = n
        self.iter = range(len(self))

        # initialisation methods
        self.generate_array()

    def generate_array(self):
        """generate the structure of the board in self.array based on the size self.size"""
        if type(self.cells) is tuple:
            raise Exception('The board has already been generated')
        edges = len(self) // 2 + len(self) % 2
        for i in self.iter:
            for j in self.iter:
                if abs(j - i) < edges:
                    self[i, j] = None
                    self.cells.append((i, j))
        self.cells = tuple(self.cells)  # lock the cells

    # special methods
    def __repr__(self):
        """print(self) : return a simple string version of the board"""
        out = '# ' + ' '.join(f'{j}' for j in self.iter)  # generate the number on the top
        for i in self.iter:
            out += f'\n{i} '
            for j in self.iter:
                if (i, j) in self:
                    if self[i, j] is None:
                        out += '*'  # empty cell
                    else:
                        out += '+'  # cell with something on it
                else:
                    out += ' '  # not a cell
                out += ' '  # spacer
        return out

    def __len__(self):
        """len(self) : return the size of the board"""
        return self.size

    def __getitem__(self, item):
        """self[i, j] : return the object on the cell (i, j)"""
        return self.array[item]

    def __setitem__(self, key, value):
        """self[i, j] = value : update the value from the cell (i, j)"""
        self.array[key] = value

    def __contains__(self, item):
        """item in self : return True if the item is the pos of a cell"""
        return item in self.cells
