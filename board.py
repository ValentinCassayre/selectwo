# -*- coding: utf-8 -*-
"""Contains the Board class"""
from insects import insect_list
from color import Color
from constants import NUMBERS


class Board:
    """Board class"""

    # one use methods
    def __init__(self):
        """constructor"""
        # initialisation of the variables with no value
        self.array = {}
        self.cells = []

        # initialisation of the values
        self.size = 9
        self.width = len(self) // 2 + len(self) % 2  # smallest possible line/raw on the board
        self.diagonals = 2 * self.width - 1  # number of diagonals from the furthest point
        self.edge = self.size - self.width + 1  # length of the diagonal from the side
        self.iter = range(len(self))

        # initialisation methods
        self.generate_array()

    def generate_array(self):
        """generate the structure of the board in self.array based on the size self.size"""
        if type(self.cells) is tuple:
            raise Exception('The board has already been generated')
        for i in self.iter:
            for j in self.iter:
                if abs(j - i) < self.width:
                    self[i, j] = None
                    self.cells.append((i, j))
        self.cells = tuple(self.cells)  # lock the cells

    # loading and saving board methods
    def from_cvn(self, cvn='5/6/7/8/9/8/7/6/5'):
        """convert a cvn string to the board"""
        cvn = cvn.split('/')
        if self.diagonals != len(cvn):
            raise ValueError(f'Expected {self.diagonals} diagonals, got {len(cvn)}')
        cells = 0
        for k, diagonal in enumerate(cvn):
            i, j = self.diagonal_cursor(k)  # put the cursor on the beginning of the diagonal
            for n, key in enumerate(diagonal):
                if key in NUMBERS:
                    if len(diagonal) > 1 and diagonal[n-1] in NUMBERS:  # more than one character long number
                        key = diagonal[n-1] + key
                        i, j = i - int(diagonal[n-1]), j - int(diagonal[n-1])
                        cells -= int(diagonal[n-1])
                    i, j = i + int(key), j + int(key)
                    cells += int(key)
                else:
                    color = Color(key == key.lower())  # create a color object based on the key (lowercase or uppercase)
                    for insect in insect_list:
                        if key.lower() == insect.id():
                            self[i, j] = insect((i, j), color)
                            break
                    i, j = i + 1, j + 1
                    cells += 1
        if cells != len(self.cells):
            raise ValueError(f'Expected {len(self.cells)} cells, got {cells}')

    def to_cvn(self):
        """return the cvn of the board"""
        cvn = str()
        for k in range(2*self.width-1):
            i, j = self.diagonal_cursor(k)
            line = []
            while i < len(self) and j < len(self):
                if self[i, j] is None:
                    if len(line) > 0 and line[-1] in NUMBERS:
                        line[-1] = str(int(line[-1]) + 1)
                    else:
                        line.append('1')
                else:
                    insect = self[i, j]
                    line.append(insect.real_id())
                i, j = i + 1, j + 1
            cvn += str().join(line) + '/'
        return cvn

    def diagonal_cursor(self, k):
        """return the position of the first cell of the diagonal number k"""
        n = self.width - 1 - k
        return max(n, 0), abs(min(n, 0))

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
                        out += self[i, j].real_id()  # cell with something on it
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
        if key in self.cells or type(self.cells) is list:
            self.array[key] = value
        else:
            raise ValueError(f'Cell {key} is not on the board')

    def __contains__(self, item):
        """item in self : return True if the item is the pos of a cell"""
        return item in self.cells
