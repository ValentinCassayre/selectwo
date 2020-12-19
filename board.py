# -*- coding: utf-8 -*-
"""Contains the Board class"""
from insects import Insects
from color import Color
from constants import NUMBERS
from copy import deepcopy


class Board:
    """Board class"""

    # one use methods
    def __init__(self):
        """constructor"""
        # initialisation of the variables with no value
        self.array = {}
        self.cells = []

        self.insect = None
        self.insects = []

        # initialisation of the values
        self.size = 9
        self.width = len(self) // 2 + len(self) % 2  # smallest possible line/raw on the board
        self.diagonals = 2 * self.width - 1  # number of diagonals from the furthest point
        self.edge = self.size - self.width + 1  # length of the diagonal from the side
        self.iter = range(len(self))

        self.game = False
        self.setback = False
        # self.capture = False
        self.turn = Color()
        self.caption = ''

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

    def reset_board(self):
        """remove everything on the board"""
        for pos in self.cells:
            self[pos] = None

    # loading and saving board methods
    def from_cvn(self, cvn='5/g4G/sg3GS/tlg2GLT/abbg1GBBA/tlg2GLT/sg3GS/g4G/5', update=True):
        """convert a cvn string to the board"""
        self.reset_board()  # clean the board
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
                    for insect in Insects:
                        if key.lower() == insect.id():
                            self[i, j] = insect((i, j), color, self)
                            break
                    i, j = i + 1, j + 1
                    cells += 1
        if cells != len(self.cells):
            raise ValueError(f'Expected {len(self.cells)} cells, got {cells}')

        if update:
            self.update()

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

    def update(self):
        """update and calculate the moves of each insects"""
        self.insects = []
        for pos in self.cells:
            if self[pos] is not None:
                insect = self[pos]
                insect.update_check()
                self.insects.append(insect)

    def check(self):
        """check if there is any setback or possible move"""
        moves = 0
        for insect in self.insects:
            if insect.color == self.turn:
                moves += len(insect.moves)
            else:
                for pos in insect.moves:
                    if self[pos] is not None:
                        attacked_insect = self[pos]
                        if attacked_insect.leader:
                            self.caption = 'setback'
                            self.setback = True
                            if len(attacked_insect.moves) == 0:
                                self.caption = 'capture'
                                self.game = False
        if moves == 0:
            self.caption = 'no moves'
            self.game = False

    def illegal_moves(self):
        """remove illegal moves"""
        array = deepcopy(self.array)
        for insect in self.insects:
            if insect.color == self.turn:
                for pos in insect.moves:
                    self.move(old_pos=insect.pos, new_pos=pos, simulation=True)
                    if self.setback:
                        print(pos)
                        insect.moves.remove(pos)
                    self.recover(array)

    def recover(self, array):
        """repair a board from an array"""
        for pos in self.cells:
            self[pos] = array[pos]
        self.caption = ''
        self.setback = False

    def select(self, pos):
        """select the insect on this cell"""
        if self[pos] is not None:
            insect = self[pos]
            if insect.color == self.turn:
                self.insect = insect

    def move(self, new_pos, old_pos=None, legit=True, turn=True, simulation=False):
        """move an insect"""
        if old_pos is None:
            old_pos = self.insect.pos

        legit = legit and new_pos in self[old_pos].moves or not legit
        turn = turn and self[old_pos].color == self.turn or not turn
        if self[new_pos] is None or self[new_pos].color != self.turn:
            if legit and turn:
                self[new_pos] = self[old_pos]
                self[old_pos] = None
                if not simulation:
                    self.insect = None
                    self[new_pos].pos = new_pos
                    self.change_turn()
        else:
            self.caption = 'unavailable move'

    def change_turn(self):
        """change turn"""
        self.turn.change()
        self.calcs()

    def calcs(self):
        """calculate moves"""
        self.check()
        self.illegal_moves()
        self.update()

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
        out += self.caption
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

    def __copy__(self):
        new = type(self)()
        new.__dict__.update(self.__dict__)
        return new
