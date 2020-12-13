# -*- coding: utf-8 -*-
"""Contain the Board class"""


class Board:
    """Board class"""

    def __init__(self, n=10):
        """constructor"""
        self.array = {}
        self.size = n
        self.generate_array()

    def generate_array(self):
        """generate the structure of the board in self.array based on the size self.size"""
        edges = self.size // 2 + self.size % 2
        for i in range(self.size):
            for j in range(self.size):
                if abs(j - i) < edges:
                    self.array[(i, j)] = None

    def __repr__(self):
        """return a simple string version of the board"""
        out = '# '
        out += ' '.join(f'{j}' for j in range(self.size))
        for i in range(self.size):
            out += '\n'
            out += f'{i} '
            for j in range(self.size):
                if (i, j) in self.array:
                    out += '*'
                else:
                    out += ' '
                out += ' '
        return out
