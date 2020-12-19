# -*- coding: utf-8 -*-
"""Contains the Insects classes"""


class Insect:
    """Mother of all the insects classes, should not be used on the board"""

    # one use methods
    def __init__(self, pos, color, board):
        # initialisation
        self.position = None
        self.color = color
        self.board = board
        self.moves = None
        self.ways = []
        self.directions = []
        self.eats = []
        self.range = range(1, len(self.board))

        # class property
        self.leader = False

        # update pos
        self.pos = pos

    def _get_position(self):
        return self.position

    def _set_position(self, new_pos):
        self.position = new_pos
        self.update()

    pos = property(_get_position, _set_position)

    def update(self):
        """update the possible positions of the insect, independently of the other insects"""
        pass

    def update_check(self):
        """remove impossible moves"""
        self.moves = []
        for pos in self.ways:
            if pos in self.board.cells and self.board[pos] is None:
                self.moves.append(pos)
        for direction in self.directions:
            for pos in direction:
                if pos in self.board.cells:
                    if self.board[pos] is not None:
                        if self.board[pos].color != self.color:
                            self.moves.append(pos)
                        break
                    self.moves.append(pos)

        for pos in self.eats:
            if pos in self.board.cells:
                if self.board[pos] is not None and self.board[pos].color != self.color:
                    self.moves.append(pos)

    def __repr__(self):
        return f'{self.color} {self.id(name=True)} in pos {self.pos}'

    def real_id(self, name=False):
        """return non-static information about the class"""
        if self.color:
            return self.id(name)
        else:
            return self.id(name).upper()

    @staticmethod
    def id(name=False):
        """return static information about the class"""
        if name:
            return 'insect'
        return 'z'


class Bug(Insect):
    """Bug insect"""

    # one use methods
    def __init__(self, pos, color, board):
        Insect.__init__(self, pos, color, board)

    def update(self):
        """update the possible positions of the insect, independently of the other insects"""
        i, j = self.pos
        d = self.color.direction()  # 1 or -1
        self.ways = [(i + d, j + d)]
        self.directions = []
        self.eats = [(i + d, j), (i, j + d)]
        self.board.update()

    @staticmethod
    def id(name=False):
        """return information about the class"""
        if name:
            return 'bug'
        return 'g'


class Locust(Insect):
    """Locust insect"""

    # one use methods
    def __init__(self, pos, color, board):
        Insect.__init__(self, pos, color, board)

    def update(self):
        """update the possible positions of the insect, independently of the other insects"""
        i, j = self.pos
        self.ways = []
        self.directions = [[(i + 1, j + 2)], [(i - 1, j - 2)], [(i + 1, j - 1)],
                           [(i + 2, j + 1)], [(i - 2, j - 1)], [(i - 1, j + 1)]]
        self.eats = []
        self.board.update()

    @staticmethod
    def id(name=False):
        """return information about the class"""
        if name:
            return 'locust'
        return 'l'


class Spider(Insect):
    """Spider insect"""

    # one use methods
    def __init__(self, pos, color, board):
        Insect.__init__(self, pos, color, board)

    def update(self):
        """update the possible positions of the insect, independently of the other insects"""
        i, j = self.pos
        self.ways = []
        self.directions = [[(i + k, j) for k in self.range],
                           [(i, j + k) for k in self.range],
                           [(i - k, j) for k in self.range],
                           [(i, j - k) for k in self.range]]
        self.eats = []
        self.board.update()

    @staticmethod
    def id(name=False):
        """return information about the class"""
        if name:
            return 'spider'
        return 's'


class Beetle(Insect):
    """Ant insect"""

    # one use methods
    def __init__(self, pos, color, board):
        Insect.__init__(self, pos, color, board)

    def update(self):
        """update the possible positions of the insect, independently of the other insects"""
        i, j = self.pos
        self.ways = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
        self.directions = [[(i + k, j + k) for k in self.range],
                           [(i - k, j - k) for k in self.range]]
        self.eats = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
        self.board.update()

    @staticmethod
    def id(name=False):
        """return information about the class"""
        if name:
            return 'beetle'
        return 't'


class Bee(Insect):
    """Bee insect"""

    # one use methods
    def __init__(self, pos, color, board):
        Insect.__init__(self, pos, color, board)

    def update(self):
        """update the possible positions of the insect, independently of the other insects"""
        i, j = self.pos
        self.ways = []
        self.directions = [[(i + k, j) for k in self.range],
                           [(i, j + k) for k in self.range],
                           [(i - k, j) for k in self.range],
                           [(i, j - k) for k in self.range],
                           [(i + k, j + k) for k in self.range],
                           [(i - k, j - k) for k in self.range]]
        self.eats = []
        self.board.update()

    @staticmethod
    def id(name=False):
        """return information about the class"""
        if name:
            return 'bee'
        return 'b'


class Ant(Insect):
    """Ant insect"""

    # one use methods
    def __init__(self, pos, color, board):
        Insect.__init__(self, pos, color, board)
        self.leader = True

    def update(self):
        """update the possible positions of the insect, independently of the other insects"""
        i, j = self.pos
        self.ways = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
        self.directions = []
        self.eats = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
        self.board.update()

    @staticmethod
    def id(name=False):
        """return information about the class"""
        if name:
            return 'ant'
        return 'a'


Insects = Bug, Locust, Spider, Beetle, Bee, Ant
